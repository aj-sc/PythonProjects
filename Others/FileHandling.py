import requests
import csv

url = 'https://jsonplaceholder.typicode.com/comments'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if data:
        filteredData = data[:20]

        # Store all CSV rows in a list
        csvRows = []

        # Optional: Add header
        csvRows.append(['postId', 'id', 'name', 'email'])

        for comment in filteredData:
            csvRows.append([
                comment['postId'],
                comment['id'],
                comment['name'],
                comment['email']
            ])

        file_path = 'C:/Users/Albert Salas/Desktop/ApiToCSV.csv'

        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(csvRows)

        print("CSV file created successfully!")