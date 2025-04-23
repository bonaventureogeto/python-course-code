# name, phone
# {
# "name": "Jane Doe",
# "phone": "011345689"
# }
contacts = []

def display_menu():
    print("\n -- Contact Book --")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

names_set = set()

def add_contact():
    name = input("Enter name: ").strip().title()
    if name in names_set:
        print("Contact already exists")
        return
    phone = input("Enter phone number: ").strip()
    contact = {
        "name": name,
        "phone": phone
    }
    contacts.append(contact)
    names_set.add(name)
    print(f"{name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    print("\n-- All Contacts --")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_name = input("Enter name to search: ").strip().title()
    found = False
    for contact in contacts:
        if contact['name'] == search_name:
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True
            break
    if not found:
        print("Contact not found")

while True:
    display_menu()
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice. Please try again!")
