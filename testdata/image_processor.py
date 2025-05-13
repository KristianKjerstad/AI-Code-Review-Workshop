# FILE: image_processor.py

from PIL import Image
import os

def resize_images(directory):
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            try:
                img = Image.open(os.path.join(directory, file))
                img = img.resize((800, 600))
                img.save(os.path.join(directory, f'resized_{file}'))
            except Exception as e:
                print(f'Failed to process {file}', e)

def main():
    path = './images'
    resize_images(path)

main()
