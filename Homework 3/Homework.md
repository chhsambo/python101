# Homework

We request API data from https://pomber.github.io/covid19/timeseries.json

```python
import requests
 
covid = requests.get("https://pomber.github.io/covid19/timeseries.json")
covid_data = covid.json()
```

This request will get covid data of all countries.

1. Write code to save data of Cambodia to CSV file
2. Save this JSON data to JSON file
3. Save this JSON data to Pickle file
