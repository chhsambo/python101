import requests
import json

covid = requests.get("https://pomber.github.io/covid19/timeseries.json")
covid_data = covid.json()

with open('covid.json', 'w') as outfile:
    json.dump(covid_data, outfile)
                