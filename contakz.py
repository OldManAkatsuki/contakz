import json


def display_contact(contacts):
    for contact in contacts:
        print()
        print('{} {}'.format(contact['first_name'], contact['last_name']))
        print(contact['phone_number'])
        print(contact['email'])
        print(contact['facebook'])


def get_contact():
    first_name = input('Input first name >> ')
    last_name = input('Input last name >> ')
    phone_number = input('Input phone number >> ')
    email = input('Input E-mail >> ')
    facebook = input('Input Facebook username >> ')

    contact = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'email': email,
        'facebook': 'facebook.com/{}'.format(facebook),
    }

    return contact


def find(contacts, prompt):
    search_contacts = input(prompt)
    results = []
    for contact in contacts:
        for item in contact.values():
            if search_contacts.lower() in item.lower(): 
                results.append(contact)
                break
    return results

def search(contacts):
    results = find(contacts, prompt='Search for >> ')
    if results:
        display_contact(results)
    else:
        print('Contact not found')



def save(contacts):
    with open('contacts.json', 'w') as f:
        f.write(json.dumps(contacts))


def load():
    with open('contacts.json', 'r') as f:
        return json.loads(f.read())


def delete_contact(contacts):
    results = find(contacts, prompt='Delete >> ')
    if not results:
        print('No contact found to delete.')
        return
    if len(results) == 1:
        _delete_contact(results[0], contacts)
    else:
        print("Which contact do you want to remove?")
        for idx, contact in enumerate(results, 1):
            print('{}. {} {}'.format(idx, contact['first_name'], contact['last_name']))
        selection = input('>> ')
        _delete_contact(results[int(selection) - 1], contacts)


def _delete_contact(contact, contacts):
    valid = False
    while not valid:
        confirm = input('Are you sure you want to delete {} {}?  y/n >> '.format(contact['first_name'], contact['last_name'])).lower()
        if confirm in ['y', 'n']:
            valid = True
        else:
            print('Invalid input')
    if confirm == 'y':
        contacts.remove(contact)


def menu():
    print('1. Add contact')
    print('2. List contacts')
    print('3. Find contact')
    print('4. Save')
    print('5. Delete')
    print('q. Quit')
    choice = input('>> ')
    return choice

# ---------------------------------------------------------------------
contacts = load()

while True:

    action = menu()

    if action == '1':
        contacts.append(get_contact())
    if action == '2':
        display_contact(contacts)
    if action == '3':
        search(contacts)
    if action == '4':
        save(contacts)
    if action == '5':
        delete_contact(contacts)
    if action == 'q':
        break
