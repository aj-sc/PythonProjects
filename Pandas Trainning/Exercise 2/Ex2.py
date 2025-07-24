import pandas as pd
import requests

baseUrl = 'https://dummyjson.com/products'

response = requests.get(baseUrl)

data = response.json()

df = pd.json_normalize(data['products'])

df['discountAmount'] = (df['price'] * df['discountPercentage']) / 100

df = df.groupby(by='category')[['price', 'discountAmount']].mean()

df.to_csv('Exercise 2/productSummary.csv')