import requests
import csv
import re

baseUrl = 'https://jsonplaceholder.typicode.com/comments'

response = requests.get(baseUrl)

if response.status_code == 200:
    baseData = response.json()

    commentsCSV = []

    commentsCSV.append(['postId', 'id', 'name', 'email', 'body'])

    for dataRow in baseData:
        email = dataRow.get('email', '')
        emailDomain = email.split(".")

        if emailDomain[-1] == 'biz':
            postId = dataRow.get('postId', '')
            id = dataRow.get('id', '')
            name = dataRow.get('name', '')
            body = re.sub(r'[^a-zA-Z0-9\s]', '', dataRow.get('body', '')).lower()

            commentsCSV.append([postId, id, name, email, body])

    file_path = 'C:/Users/Albert Salas/Desktop/bizPosts.csv'

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(commentsCSV)
        print('CSV Created')