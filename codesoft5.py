import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contacts = load_contacts()
    
    # Check for duplicate phone number
    for contact in contacts:
        if contact["phone"] == phone:
            print("Contact with this phone number already exists!\n")
            return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!\n")

# Function to view all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

# Function to search for a contact
def search_contact():
    search_query = input("Enter Name or Phone Number to search: ").strip()
    contacts = load_contacts()
    results = [c for c in contacts if search_query.lower() in c["name"].lower() or search_query in c["phone"]]

    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    else:
        print("No matching contact found.\n")

# Function to update a contact
def update_contact():
    phone = input("Enter the phone number of the contact to update: ").strip()
    contacts = load_contacts()

    for contact in contacts:
        if contact["phone"] == phone:
            print("\nEnter new details (press Enter to keep current values):")
            contact["name"] = input(f"Name ({contact['name']}): ").strip() or contact["name"]
            contact["email"] = input(f"Email ({contact['email']}): ").strip() or contact["email"]
            contact["address"] = input(f"Address ({contact['address']}): ").strip() or contact["address"]
            save_contacts(contacts)
            print("Contact updated successfully!\n")
            return

    print("Contact not found!\n")

# Function to delete a contact
def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ").strip()
    contacts = load_contacts()

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found!\n")

# Main menu
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.\n")

# Run the application
if __name__ == "__main__":
    main()
