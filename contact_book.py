contacts = {}

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact added!")
    
    elif choice == '2':
        for name, info in contacts.items():
            print(f"\nName: {name}")
            for key, value in info.items():
                print(f"{key}: {value}")
    
    elif choice == '3':
        search = input("Enter name to search: ")
        if search in contacts:
            print(f"\nFound: {search}")
            for key, value in contacts[search].items():
                print(f"{key}: {value}")
        else:
            print("Contact not found.")
    
    elif choice == '4':
        delete = input("Enter name to delete: ")
        if delete in contacts:
            del contacts[delete]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    
    elif choice == '5':
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice.")
