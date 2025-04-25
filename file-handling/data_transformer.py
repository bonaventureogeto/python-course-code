import csv, json

# step 1: Read names
with open("names.txt", "r") as file:
    names = file.read().strip().split(",")
    print(names)

# step 2: write to csv
with open("names.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow("Names")
    for name in names:
        writer.writerow([name])

# step3: write to JSON
with open("names.json", "w") as file:
    json.dump({"names": names}, file, indent=2)
