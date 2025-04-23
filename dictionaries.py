my_dict = {
    "name": "Alice",
    "age": 12,
    "is_student": True
}

person = {
    "name": "Pablo",
    "age": 45,
    "job": "Engineer"
}

person1 = dict(name="Jake", age=34, job="Teacher")

# print(person["age"])
# print(person.get("job", "Not specified"))

person["status"] = "Married"
person["age"] = 49
# print(person["age"])

person.pop("job")
del person["status"]
# print(person["status"])

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key} -> {value}")

"""
Create a dictionary called 'student' with keys: 'name', 'grade', 'courses'
Then, add a new key 'graduated' with values of 'False'.
"""

# project -> build a simple phonebook dictionary and allow users to look up contacts
