import requests
import pickle

covid = requests.get("https://pomber.github.io/covid19/timeseries.json")
covid_data = covid.json()

pickle_file = open("covid.pickle","wb")
pickle.dump(covid_data, pickle_file)
pickle_file.close()                