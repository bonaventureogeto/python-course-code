# 📂 Python File Handling - Beginner Notes

Welcome!
This guide covers the **basics of file handling in Python**, including how to **read** and **write** files in different formats like **TXT**, **CSV**, and **JSON**.

---

## ✍️ 1. Working with Text Files (.txt)

**Opening and Writing to a Text File**

```python
# Write to a file (overwrite if exists)
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Python file handling is easy.")
```

- `"w"` = Write mode. Creates the file if it doesn't exist, or **overwrites** if it does.
- `with open(...) as file:` automatically **closes** the file for you.

**Reading from a Text File**

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

- `"r"` = Read mode.

> ✅ Tip: Always use `with` to open files — it handles closing the file even if an error occurs!

---

## 📈 2. Working with CSV Files (.csv)

Python provides a built-in module called **`csv`** to handle CSV (Comma-Separated Values) files.

**Writing to a CSV File**

```python
import csv

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "Nairobi"])
```

- `newline=""` prevents inserting blank rows (especially on Windows).

**Reading from a CSV File**

```python
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

**Bonus:** Using a `DictWriter` for structured writing:

```python
writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
writer.writeheader()
writer.writerow({"Name": "Alice", "Age": 25, "City": "New York"})
```

---

## 📦 3. Working with JSON Files (.json)

**JSON** (JavaScript Object Notation) is a format used to store and exchange data, often between web services.

Python uses the built-in **`json`** module.

**Writing JSON Data to a File**

```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Analysis"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
```

- `indent=4` makes the JSON file pretty and readable.

**Reading JSON Data from a File**

```python
with open("data.json", "r") as file:
    content = json.load(file)
    print(content)
```

---

## ⚡ Quick Summary: File Modes in Python

| Mode | Description |
|:----:|:------------|
| `"r"` | Read (default mode). Error if file doesn't exist. |
| `"w"` | Write. Creates a new file or overwrites an existing file. |
| `"a"` | Append. Adds data to the end of the file if it exists. |
| `"x"` | Create. Fails if the file already exists. |
| `"rb"` | Read in binary mode. |
| `"wb"` | Write in binary mode. |

---

## 🛠️ Mini Project Idea: Data Transformer

- Read a `.txt` file containing names separated by commas.
- Save the names into both a `.csv` and a `.json` file.

```python
# Reading names from txt
with open("names.txt", "r") as f:
    names = f.read().strip().split(",")

# Writing names to csv
with open("names.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name"])
    for name in names:
        writer.writerow([name])

# Writing names to json
with open("names.json", "w") as f:
    json.dump({"names": names}, f, indent=2)
```

---

# 🎯 Key Takeaways
- Always use the `with open(...) as ...` pattern.
- Understand file formats: `.txt` for plain text, `.csv` for spreadsheets, `.json` for structured data.
- Master basic read/write operations before moving to advanced topics like error handling, large file processing, or APIs.

---

### 📚 Resources
- [Python `open()` documentation](https://docs.python.org/3/library/functions.html#open)
- [Python `csv` module documentation](https://docs.python.org/3/library/csv.html)
- [Python `json` module documentation](https://docs.python.org/3/library/json.html)
