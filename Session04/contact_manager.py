# Session 4: 04/08/2026
contacts = [
    {
    "name": "Alice Smith",
    "phone": "123-456-7890",
    "email": "alice@gmail.com",
    "tags": ["friend", "work"]
    },
    {
    "name": "Bob Johnson",
    "phone": "987-654-3210", 
    "email": "bob@gmail.com",
    "tags": ["family"]
    },
    {
    "name": "Charlie Brown",
    "phone": "555-555-5555",
    "email": "charlie@gmail.com",
    "tags": ["friend"]
    }
]

MAX_CONTACTS = 100
def add_contact(contacts, name, phone, email, tags=None):
    if len(contacts) >= MAX_CONTACTS:
        print(f"Contacts is full. Maximum number of contacts reached. {MAX_CONTACTS} contacts allowed.")
        return
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "tags": tags if tags else []
    }

    contacts.append(new_contact)
    print(f"Contact '{name}' added successfully.")

def search_contacts(contacts, query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query.lower() in contact['email'].lower()]
    return results

def display_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    
    sorted_contacts = sorted(contacts, key=lambda x: x['name'])
    for idx, contact in enumerate(sorted_contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Tags: {', '.join(contact.get('tags', []))}")

def get_all_tags(contacts):
    tags = set()
    for contact in contacts:
        for tag in contact.get('tags', []):
            tags.add(tag)  
    return tags

def delete_contact(contacts, name):
    for i,contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            contacts.pop(i)
            print(f"Contact '{name}' deleted successfully.")
            return
    print(f"Contact '{name}' not found.")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. Display Contacts")
        print("4. Get All Tags")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            tags_input = input("Enter tags (comma separated): ")
            tags = [tag.strip() for tag in tags_input.split(',')] if tags_input else []
            add_contact(contacts, name, phone, email, tags)
        
        elif choice == '2':
            query = input("Enter search query: ")
            results = search_contacts(contacts, query)
            if results:
                print(f"Found {len(results)} contact(s):")
                for contact in results:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Tags: {', '.join(contact.get('tags', []))}")
            else:
                print("No contacts found.")
        
        elif choice == '3':
            display_contacts(contacts)
        
        elif choice == '4':
            tags = get_all_tags(contacts)
            if tags:
                print(f"All Tags: {', '.join(tags)}")
            else:
                print("No tags found.")
        
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
        
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()