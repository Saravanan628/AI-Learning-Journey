import json
from typing import List, Dict

class ContactBook:
    """Simple contact book that stores contacts in a JSON file"""
    def __init__(self,filename: str="contacts.json"):
        self.filename=filename
        self.contacts:List[Dict]=[]
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as f:
                self.contacts=json.load(f)
        except FileNotFoundError:
            self.contacts=[]
        except json.JSONDecodeError:
            print("File is corrupted! start fresh")
            self.contacts=[]

    def save_Contacts(self):
        with open(self.filename, "w") as f:
            json.dump(self.contacts,f, indent=4)

    def add_contact(self,name,phone,email):
        contact={
            "name":name,
            "phone":phone,
            "email":email
        }
        self.contacts.append(contact)
        self.save_Contacts()
        print(f"Contact added successfully")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return

        print("\n--- All Contacts ---")
        for i, c in enumerate(self.contacts, start=1):
            print(f"{i}. Name: {c['name']}, Phone: {c['phone']}, Email: {c.get('email', '')}")
        print("--------------------")

    def search_contact(self, name) :
        results = [
            c for c in self.contacts
            if c["name"].lower() == name.lower()
        ]

        if not results:
            print(f"No contact found with name '{name}'.")
            return

        print(f"\nContacts matching '{name}':")
        for c in results:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c.get('email', '')}")

    def delete_contact(self, name):
        original_len = len(self.contacts)
        self.contacts = [
            c for c in self.contacts
            if c["name"].lower() != name.lower()
        ]

        if len(self.contacts) == original_len:
            print(f"No contact found with name '{name}'.")
        else:
            self.save_contacts()
            print(f"Contact(s) with name '{name}' deleted successfully.")

def main():
    book = ContactBook()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add contact")
        print("2. List all contacts")
        print("3. Search contact by name")
        print("4. Delete contact by name")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email (optional): ").strip()
            book.add_contact(name, phone, email)

        elif choice == "2":
            book.list_contacts()

        elif choice == "3":
            name = input("Enter name to search: ").strip()
            book.search_contact(name)

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            book.delete_contact(name)

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
