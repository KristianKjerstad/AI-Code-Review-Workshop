# FILE: data_pipeline.py

import pandas as pd
import json
import os

class DataPipeline:
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = None
        self.cleaned_data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.input_file)
        except:
            print("Failed to load data")

    def clean_data(self):
        self.cleaned_data = self.data.dropna()
        self.cleaned_data.columns = [x.lower() for x in self.cleaned_data.columns]
        for col in self.cleaned_data.columns:
            if 'date' in col:
                self.cleaned_data[col] = pd.to_datetime(self.cleaned_data[col])

    def save_as_json(self, output_path):
        records = self.cleaned_data.to_dict(orient='records')
        with open(output_path, 'w') as f:
            f.write(json.dumps(records))

    def run_pipeline(self, output_path):
        self.load_data()
        self.clean_data()
        self.save_as_json(output_path)

if __name__ == '__main__':
    pipeline = DataPipeline('input.csv')
    pipeline.run_pipeline('cleaned.json')
