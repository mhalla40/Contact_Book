from peewee import *
from datetime import date

db = PostgresqlDatabase('book', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = CharField()
    birthday = DateField()


db.drop_tables([Contact])
db.create_tables([Contact])

michael = Contact(first_name='Michael', last_name='Hall',
                  phone='555-5555', birthday=date(1985, 2, 20))
michael.save()

kim = Contact(first_name='Kim', last_name='Locks',
              phone='510-5555', birthday=date(1987, 3, 15))
kim.save()

steve = Contact(first_name='Steve', last_name='McQueen',
                phone='525-5555', birthday=date(1985, 8, 30))
steve.save()

lisa = Contact(first_name='Lisa', last_name='Bonet',
               phone='545-5555', birthday=date(1986, 1, 17))
lisa.save()


def contact_book():
    print('  1: Contacts \n 2: Make Contact \n 3: Update Contact \n 4: Delete Contact \n 5: Exit')
    choice = input('Enter the category: ')
    if choice == '1':
        contact()
    elif choice == '2':
        make_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    else:
        exit()


def contact():
    people = Contact.select()
    for contact in people:
        print(contact.first_name)
    name = input("Enter name or type 'exit' to go to main menu: ")
    if name == 'exit':
        contact_book()
    contact = Contact.get(Contact.first_name == name)
    print(
        f'Full Name: {contact.first_name} {contact.last_name} \n Phone Number: {contact.phone} \n Birthday: {contact.birthday}')
    contact_book()


def make_contact():
    new_first_name = input('Enter First name: ')
    new_last_name = input('Enter last name: ')
    new_phone_number = input('Enter phone number: ')
    new_birthday = input('Enter birthday: ')

    add_contact = Contact(
        first_name=new_first_name,
        last_name=new_last_name,
        phone=new_phone_number,
        birthday=new_birthday
    )

    add_contact.save()
    contact_book()


def update_contact():
    people = Contact.select()
    for contact in people:
        print(contact.first_name)
    name = input('Enter name to update: ')
    if name == Contact.first_name:
        print('1: First Name \n 2: Last Name \n 3: Phone Number \n 4: Birthday')
        choice = input('Enter number to update: ')
        if choice == '1':
            contact = Contact.get(Contact.first_name == name)
            contact.first_name = input('New First Name: ')
            contact.save()
            contact_book()
        elif choice == '2':
            contact = Contact.get(Contact.first_name == name)
            contact.last_name = input('New Last Name: ')
            contact.save()
            contact_book()
        elif choice == '3':
            contact = Contact.get(Contact.first_name == name)
            contact.phone = input('New Phone Number: ')
            contact.save()
            contact_book()
        elif choice == '4':
            contact = Contact.get(Contact.first_name == name)
            contact.birthday = input('New Birthday: ')
            contact.save()
            contact_book()
        else:
            contact_book()


def delete_contact():
    people = Contact.select()
    for contact in people:
        print(contact.first_name)
    out = input('Choose contact to delete: ')
    if out == Contact.first_name:
        done = input('Are you sure you want to delete? y/n: ')
        if done == 'y':
            contact = Contact.get(Contact.first_name == out)
            contact.delete_instance()
            contact_book()
        else:
            delete_contact()
    else:
        contact_book()


contact_book()
