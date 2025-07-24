import json

user_data = {
    "user1": {
        "name": "Alice Smith",
        "age": 30,
        "skills": ["Python", "Data Analysis", "Machine Learning"]
    },
    "user2": {
        "name": "Bob Johnson",
        "age": 24,
        "skills": ["JavaScript", "React", "Web Development", "UI/UX Design"]
    },
    "user3": {
        "name": "Charlie Brown",
        "age": 35,
        "skills": ["Project Management", "Agile Methodologies", "Team Leadership"]
    },
    "user4": {
        "name": "Diana Prince",
        "age": 28,
        "skills": ["Graphic Design", "Illustration", "Video Editing"]
    },
    "user5": {
        "name": "Ethan Hunt",
        "age": 42,
        "skills": ["Cybersecurity", "Network Administration", "Cloud Computing"]
    }
}

file_path = 'C:\\Users\\Albert Salas\\Desktop\\jsonTest.json'

with open(file_path, 'w') as file:
    json.dump(user_data, file, indent=4)

with open(file_path, 'r') as file:
    content = json.load(file)
    fomattedContent = json.dumps(content, indent=4)
    print(fomattedContent)