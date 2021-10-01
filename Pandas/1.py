import pandas as pd
import requests

poke = pd.read_csv('pokemon_data.csv')


print(poke)
print(poke.head(3))
print(poke.tail(3))


r= requests.Po