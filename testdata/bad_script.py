# FILE: bad_script.py

import os, sys

def processData(items):
    results = []
    for i in range(len(items)):
        if items[i] != None:
            results.append(items[i]*2)
        else:
            continue
    return results

def main():
    data = [1, 2, None, 4]
    print("Results:")
    print(processData(data))

main()
