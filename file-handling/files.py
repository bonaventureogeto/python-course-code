import csv
from csv import DictWriter
import json

# with open("notes.txt", "w") as file:
#     file.write("Learn Python with me!\n")
#     file.write("Files are super useful.\n")

# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("users.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
#     writer.writerow({"Name":"Alice", "Age": 25,"City": "Nairobi"})

# with open("users.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "JavaScript"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    content = json.load(file)
    print(f"JSON Data: {content}")
