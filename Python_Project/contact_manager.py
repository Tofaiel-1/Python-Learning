import csv
import os

def save_contacts(contacts):
    with open('contacts.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Email', 'Birthdate', 'Note', 'District','Police_Station','Post_Office','Post_Code','Present_Address','Premanent_Address', 'Bank_Account_Number', 'Facebook_ID', 'Linkedin_ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

def load_contacts():
    contacts = []
    if os.path.exists('contacts.csv'):
        with open('contacts.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append(row)
    return contacts

def add_contact(contacts):
    name = input("Name: ")
    email = input("Email: ")
    birthdate = input("Birthdate: ")
    note = input("Note: ")
    district = input("District: ")
    police_station = input("police station: ")
    post_office = input("post_office:")
    post_code = input('Post_code:')
    present_address =input("present_address:")
    permanent_address = input("Permanent Address:")
    bank_account_number = input("Bank Account Number:")
    facebook_id = input("Facebook ID: ")
    linkedin_id = input("Linkedin ID: ")

    contact = {
        'Name': name,
        'Email': email,
        'Birthdate': birthdate,
        'Note': note,
        'District': district,
        'Police station':police_station,
        'Post_Office':post_office,
        'Post_code':post_code,
        "Present_Address":permanent_address,
        "Permanent_Address":permanent_address,
        'Bank_Account_Number': bank_account_number,
        'Facebook_ID': facebook_id,
        'Linkedin_ID': linkedin_id
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def delete_contact(contacts):
    name_to_delete = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['Name'] == name_to_delete:
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact '{name_to_delete}' deleted successfully.")
            return
    print(f"Contact '{name_to_delete}' not found.")

def search_contact(contacts):
    search_term = input("Enter a name or email to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term.lower() in contact['Email'].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Search results:")
        for contact in found_contacts:
            print(contact)
    else:
        print("No matching contacts found.")

def display_menu():
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Exit")

def main():
    contacts = load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
