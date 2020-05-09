import requests
import csv

covid = requests.get("https://pomber.github.io/covid19/timeseries.json")
covid_data = covid.json()
cambodia_covid_data = covid_data['Cambodia']

f = open('covid.csv', 'w')
with f:
    fnames = ['date', 'confirmed', 'deaths', 'recovered']
    writer = csv.DictWriter(f, fieldnames=fnames)

    writer.writeheader()
    for data in cambodia_covid_data:
        writer.writerow(data)
                