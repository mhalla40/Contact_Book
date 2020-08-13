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
