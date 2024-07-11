contact = {}

def display_contact():
    if not contact:
        print("Empty contact book")
    else:
        print("Name\t\tContact Number\t\tEmail\t\tAddress")
        for name, details in contact.items():
            print(f"{name}\t\t{details['phone']}\t\t{details['email']}\t\t{details['address']}")

while True:
    print("\nMenu:")
    print("1. Add new contact")
    print("2. Search contact")
    print("3. Display contacts")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        email = input("Enter the email address: ")
        address = input("Enter the address: ")
        contact[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact added successfully.")
    
    elif choice == 2:
        search_name = input("Enter the contact name to search: ")
        if search_name in contact:
            print(f"{search_name}'s details:")
            print(f"Phone: {contact[search_name]['phone']}")
            print(f"Email: {contact[search_name]['email']}")
            print(f"Address: {contact[search_name]['address']}")
        else:
            print("Name not found in contact book.")
    
    elif choice == 3:
        display_contact()
    
    elif choice == 4:
        edit_contact = input("Enter the contact name to edit: ")
        if edit_contact in contact:
            phone = input("Enter new mobile number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            contact[edit_contact] = {'phone': phone, 'email': email, 'address': address}
            print("Contact updated successfully.")
            display_contact()
        else:
            print("Name not found in contact book.")
    
    elif choice == 5:
        del_contact = input("Enter the contact name to delete: ")
        if del_contact in contact:
            confirm = input(f"Do you want to delete {del_contact}? (y/n): ")
            if confirm.lower() == 'y':
                contact.pop(del_contact)
                print("Contact deleted successfully.")
                display_contact()
        else:
            print("Name not found in contact book.")
    
    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
