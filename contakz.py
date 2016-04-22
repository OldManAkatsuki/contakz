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


def save(contacts):
    with open('contacts.json', 'w') as f:
        f.write(json.dumps(contacts))


def menu():
    print('1. Add contact')
    print('2. List contacts')
    print('3. Save')
    print('q. Quit')
    choice = input('>> ')
    return choice

# ---------------------------------------------------------------------
contacts = []

while True:

    action = menu()

    if action == '1':
        contacts.append(get_contact())
    if action == '2':
        display_contact(contacts)
    if action == '3':
        save(contacts)
    if action == 'q':
        break
