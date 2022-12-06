from peewee import *

db = PostgresqlDatabase('university_bd', host='localhost', port=5432)


class BaseModel(Model):

    class Meta:
        database = db