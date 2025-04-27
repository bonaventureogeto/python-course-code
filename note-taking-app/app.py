def add_note():
    note = input("Enter a note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("\n Your notes")
                for idx, note in enumerate(notes, 1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("No notes found!")
    except FileNotFoundError:
        print("No notes file found. Start by adding a note.")

def delete_note():
    view_notes()
    try:
        note_number = int(input("\nEnter the note number to delete: "))
        with open("notes.txt", "r") as file:
            notes = file.readlines()

        if 0 < note_number <= len(notes):
            removed_notes = notes.pop(note_number - 1)
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print(f"Deleted: {removed_notes.strip()}")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number")
    except FileNotFoundError:
        print("No notes found.")

def main():
    print("Welcome to the Note-Taking-App")
    while True:
        print("""
            === Note Taking App ===
            1. Add note
            2. View notes
            3. Delete notes
            4. Exit
            """)

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
