from peewee import *

db = PostgresqlDatabase('book', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()
