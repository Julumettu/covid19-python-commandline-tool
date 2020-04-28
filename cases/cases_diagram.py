import os
import json
import sys

print("One * represents 50k-cases")

for filename in os.listdir('.'):
    if filename.endswith('.json'):
        cases_json = open(filename, mode='r', encoding='utf-8')
        data = json.load(cases_json, encoding='utf-8')
        cases_json.close()
        
        all_cases = 0

        for p in data['Countries']:
            all_cases += p['TotalConfirmed']
        all_cases = all_cases / 50000
        print("Cases in: " + filename)
        print(int(round(all_cases)) * "*")


