import csv
import requests
import datetime

base_url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    userCsv = []
    userCsv.append(["Name", "Email", "Phone", "Street", "Zipcode", "City", "Company Name", "Extract Date"])

    for userData in data:
        nameData = userData.get('name', '')
        emailData = userData.get('email', '')
        phoneData = userData.get('phone', '')
        streetData = userData.get('address', {}).get('street', '')
        zipData = userData.get('address', {}).get('zipcode', '')
        cityData = userData.get('address', {}).get('city', '')
        companyData = userData.get('company',{}).get('name', '')

        userCsv.append(
            [
                nameData,
                emailData,
                phoneData,
                streetData,
                zipData,
                cityData,
                companyData,
                timestamp
            ]
        )

file_path = 'C:/Users/Albert Salas/Desktop/userCsv.csv'

with open(file_path, 'w', newline="") as file:
    writer = csv.writer(file)
    
    for row in userCsv:
        writer.writerow(row)
    
    print('CSV Loaded')