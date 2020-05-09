import requests
import json
import pickle
import csv

covid = requests.get("https://pomber.github.io/covid19/timeseries.json")
covid_data = covid.json()

print("########### COUNTRY AFFECTED BY COVID19 ###########")
for allcovid_data in covid_data:
    print(allcovid_data,end=' | ')
xx = 0
country = input(f"\nSearch CovidNews By Country:").lower()
for allcovid_data in covid_data:
    if country in allcovid_data.lower():
        m = covid_data[allcovid_data]
        xx = 1
        x = input("\n[csv]Save File name:") + ".csv"
        with open(x ,mode='a') as out_file:
            csv_w = csv.writer(out_file)
            csv_w.writerow(m)

        y = input("\n[json]Save File name:") + ".json"
        f = open(y,mode='a',encoding='utf-8')
        json.dump(m, f, ensure_ascii=False, indent=4)

        z = input("\n[pickle]Save File name:") + ".pickle"
        f = open(z,mode='wb')
        pickle.dump(m,f,)

if xx != 1:
    print("Invalid Country")