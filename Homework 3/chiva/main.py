import csv
import json
import pickle
import requests
import os

covid=requests.get("https://pomber.github.io/covid19/timeseries.json")
covid=covid.json()

def transfom_data_csv(covid_data):
    data_list=[]
    data_list.append([key for key in covid_data['Cambodia'][0].keys()])
    data_list[0].append('country')
    data_list[0][1:]=data_list[0][0:4]  
    data_list[0][0]='country'
    temp=[]
    for item in covid_data.items():
        #print(type(item)) #item return as tuple
        #print(item[1])  # return as list( item in this list is dict )
        #print(item[0])  # return as string (key of dict)
        for item_dict in item[1]:
            #print(type(item_dict))  #return as dict
            #data_list.append(list(item_dict.values()))
            temp=list(item_dict.values())
            temp[1:]=temp[0:4]
            temp[0]=item[0]  # item[0] is key of covid_data (dict)

            data_list.append(temp)       
    return data_list

def write(data,name_file,type_file):
    dirpath = os.getcwd()
    if type_file =='csv':
        with open(f"{dirpath}/{name_file}.{type_file}",mode='w',newline="") as f:
            writer=csv.writer(f)
            writer.writerows(data)
            return 'Successfuly'
    elif type_file=='json':
        with open(f"{dirpath}/{name_file}.{type_file}",mode='w',newline="") as f:
            json.dump(data,f)
            return 'Successfuly'
    elif type_file=='pkl' or type_file=='pickle' :
        with open(f"{dirpath}/{name_file}.pkl",mode='wb') as f:
            pickle.dump(data,f)
            return 'Successfuly'
    else:
      return 'failed'

print(f"Write as csv is {write(transfom_data_csv(covid),'covid','csv')}")
print(f"Write as json is {write(covid,'covid','json')}")
print(f"Write as pickle is {write(covid,'covid','pkl')}")
