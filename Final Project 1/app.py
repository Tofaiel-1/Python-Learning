class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, email, phone):
        self.contacts[name] = {'email': email, 'phone': phone}
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Email: {details['email']}, Phone: {details['phone']}")
        else:
            print("No contacts found.")

    def update_contact(self, name, email=None, phone=None):
        if name in self.contacts:
            if email:
                self.contacts[name]['email'] = email
            if phone:
                self.contacts[name]['phone'] = phone
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

def main():
    address_book = AddressBook()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            address_book.add_contact(name, email, phone)
        elif choice == '2':
            address_book.view_contacts()
        elif choice == '3':
            name = input("Enter name of contact to update: ")
            email = input("Enter new email (press enter to skip): ")
            phone = input("Enter new phone (press enter to skip): ")
            address_book.update_contact(name, email, phone)
        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            address_book.delete_contact(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
