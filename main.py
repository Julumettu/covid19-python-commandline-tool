import json
import requests
import sys
from datetime import date
import os

if(len(sys.argv) < 2):
    print("Please specify country. For all use \"all\"")
    print("Optional argument \"no_summary\"")
    print("For example: " + sys.argv[0] + " \"Finland\" \"no_summary\"")
    print("For just the summary use: " + sys.argv[0] + " summary")
    exit()
today = date.today()
case_file_name = "cases/" + str(today) + "-cases.json"

if (os.path.isfile(case_file_name)):
    print("Todays cases already fetched skipping...")
else:
    cases = requests.get('https://api.covid19api.com/summary')
    cases.encoding = 'utf-8'
    f = open(case_file_name, mode='w')
    f.write(str(cases.text))
    f.close()

cases_json = open(case_file_name, mode='r')
data = json.load(cases_json)
cases_json.close()

search_word = sys.argv[1]
if sys.argv[1] == "all":
    search_word = ""

all_cases = 0
all_recoveries = 0
all_deaths = 0
active_cases = 0

for p in data['Countries']:
    all_cases += p['TotalConfirmed']
    all_recoveries += p['TotalRecovered']
    all_deaths += p['TotalDeaths']
    if search_word in p['Country'] and search_word != "summary":
        print("******************************************")
        print(p['Country'])
        print("Total cases: " + str(p['TotalConfirmed']))
        print("Total recoveries: " + str(p['TotalRecovered']))
        print("Total deaths: " + str(p['TotalDeaths']))
        total_active = p['TotalConfirmed'] - p['TotalRecovered'] - p['TotalDeaths']
        print("Total active cases: " + str(total_active))

if(len(sys.argv) == 3):
    if(sys.argv[2] == "no_summary"):
        exit()

print("******************************************")
print("Summary: ")
print("Total cases: " + str(all_cases))
print("Total recoveries: " + str(all_recoveries))
print("Total deaths: " + str(all_deaths))
active_cases = all_cases - all_recoveries - all_deaths
print("Total active cases: " + str(active_cases))
