def display_contacts(contacts):
    if contacts:
        print("\nYour Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    else:
        print("\nYour contact book is empty.")

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    number = input("Enter the contact's number: ")
    contacts[name] = number
    print(f"Contact '{name}' added successfully!")

def delete_contact(contacts):
    name = input("Enter the contact's name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def contact_book():
    contacts = {}
    while True:
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Delete Contact")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice == 1:
                display_contacts(contacts)
            elif choice == 2:
                add_contact(contacts)
            elif choice == 3:
                delete_contact(contacts)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Error: Please enter a valid number.")

if __name__ == "__main__":
    contact_book()
