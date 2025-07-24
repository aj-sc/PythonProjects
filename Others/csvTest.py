import csv

employees = [["Nombre", "Edad", "Peso", "Altura"], 
             ["Albert Salas", 28, "88 kg", "1.90 cm"],
             ["Esthefanny Arango", 25, "45 kg", "1.65 cm"]]

file_path = 'C:\\Users\\Albert Salas\\Desktop\\info.csv'

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print("CSV creado exitosamente")

with open(file_path, "r", newline="") as file:
    content = csv.reader(file)
    for line in content:
        print(line)
    print("CSV leido exitosamente")