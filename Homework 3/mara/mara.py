import csv
import os
import sys
import json
import pickle
import requests

Path=os.path.dirname(os.path.realpath(sys.argv[0]))

covid = requests.get("https://pomber.github.io/covid19/timeseries.json")
covid_data = covid.json()

# function for writing dictionary to csv
def write_dict_to_csv(dictionary,file_name):
    lists=[]
    lists.append([h for h in dictionary[0].keys()])
    for item in dictionary:
        lists.append(list(item.values()))
    with open(f"{Path}\{file_name}.csv",mode="w+",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(lists)

# function for writing dictionary to json
def write_dict_to_json(Country_Name):
    covid_data_by_country={Country_Name:covid_data[Country_Name]}
    with open(f"{Path}\Report of Covid-19 for {Country_Name}.json",mode="w") as f:
        json.dump(covid_data_by_country,f)

# function for writing dictionary to pkl (pickle)
def write_dict_to_pickle(Country_Name):
    covid_data_by_country={Country_Name:covid_data[Country_Name]}
    with open(f"{Path}\Report of Covid-19 for {Country_Name}.pkl",mode="wb") as f:
        pickle.dump(covid_data_by_country,f)

# function for reading pkl (pickle)
def reading_pickle(file_name):
    with open(f"{Path}\{file_name}.pkl","rb") as f:
        data=pickle.load(f)
    print(data)

# write covid-19 data of Cambodia to csv file, and file named 'Covid-19'
write_dict_to_csv(covid_data['Cambodia'],'Covid-19.csv')

# write covid-19 data of Cambodia to json file, and file named 'Report of Covid-19 for Cambodia.json'
write_dict_to_json('Cambodia')

# write covid-19 data of Cambodia to pickle file, and file named 'Report of Covid-19 for Cambodia.pkl'
write_dict_to_pickle('Cambodia')

# read pkl file 'Report of Covid-19 for Cambodia.pkl'
reading_pickle("Report of Covid-19 for Cambodia")