import requests

data = requests.get('https://openlibrary.org/api/books?bibkeys=ISBN:0201558025,LCCN:93005405&callback=processBooks')

print(data.text )