# # pip install requests
import requests

# antkh = requests.get("http://www.antkh.com")
# antkh_content = antkh.text()
covid = requests.get("https://pomber.github.io/covid19/timeseries.json")
covid_data = covid.json()

cambodia_data = covid_data["Cambodia"]

print(cambodia_data[-7:])

# print(covid_data.keys())

# Find covid information by country
# > enter: US
# > enter: Cambodia
# > enter: Thailand
# => Show last 7 days of covid information