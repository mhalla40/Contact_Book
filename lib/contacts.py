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
    contacts = Contact.select()
    for contact in contacts:
        print(
            f'Full Name: {contact.first_name} {contact.last_name} \n Phone Number: {contact.phone} \n Birthday: {contact.birthday}')
    quit = input("To go back to the Main Menu, type 'exit': ")
    if quit == 'exit':
        contact_book()


contact_book()
