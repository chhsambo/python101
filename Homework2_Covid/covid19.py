import requests
from rich.console import Console
from rich.table import Column, Table
from rich.progress import track
import time

def get_data_api(url):
    return requests.get(url).json()
def get_data_country(name):
    covid=get_data_api("https://pomber.github.io/covid19/timeseries.json")
    for i in track(range(50)):
        time.sleep(0.1)
    try:
        if(covid[name]!=None):            
            return covid[name]
    except Exception :
        console.print("Not found",style="italic red")
    return None
console=Console()
#cprint("[italic red]This program will show aboout covid report[/italic red]")   // use code BBO
console.print("_________________________Search country name_________________________",style="bold magenta")
print()

country_name=input("Input name : ")
number_day=int(input("Input number of period : "))

country_covid=get_data_country(country_name)    #return as list (that contain dict)

if country_covid!=None:
    
    table=Table(show_header=True,header_style="bold magenta")
    table.add_column("Date", style="dim" ,width=20)
    table.add_column("Confirmed", style="dim" )
    table.add_column("Deaths", style="dim" )
    table.add_column("Recovered", style="dim" )

    for item in country_covid[-number_day:] :
        table.add_row(str(item['date']),str(item['confirmed']),str(item['deaths']),str(item['recovered']))
    console.print(table)