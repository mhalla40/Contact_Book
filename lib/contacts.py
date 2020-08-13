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
