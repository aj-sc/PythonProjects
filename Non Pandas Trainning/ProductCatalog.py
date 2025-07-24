import requests
import csv

base_url = 'https://dummyjson.com/products'

userInput = int(input('How many products do you want to see ?: '))

complete_url = f'{base_url}?limit={userInput}'

response = requests.get(complete_url)

if response.status_code == 200:
    baseData = response.json()

    productData = baseData.get('products', {})

    productDataCSV = []
    productDataCSV.append(['product_id', 'name', 'brand', 'category', 'price', 'stock'])

    for product in productData:

        if product.get('price', '') < 50:
            productDataCSV.append(
            [
                product.get('id', ''),
                product.get('title', ''),
                product.get('brand', ''),
                product.get('category', ''),
                product.get('price', ''),
                product.get('stock', ''),
            ]
        )
    
    file_path = 'C:/Users/Albert Salas/Desktop/catalog.csv'

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in productDataCSV:
            writer.writerow(row)
        print('CSV Loaded')