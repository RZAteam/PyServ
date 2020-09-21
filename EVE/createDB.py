import sqlalchemy
import pymysql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from eve import Eve

from sqlalchemy.orm import column_property


from eve_sqlalchemy import SQL
from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from eve_sqlalchemy.validation import ValidatorSQL
from Tables import general, Base, ammountOfGroup, rooms, equipment, days, ranks, existanceOfEquipment, groups, lessons, numberOfWeek, teachers, time, typesOfRooms, weeks, prikazy

pymysql.install_as_MySQLdb()
# sqlalchemy.__version__
engine = sqlalchemy.create_engine('mysql://user:passwrd@localhost/RZAPlatform', echo=True)

print("Hi")

SETTINGS = {
    'DEBUG': True,
    'SQLALCHEMY_DATABASE_URI': 'mysql://user:passwrd@localhost/RZAPlatform',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'RESOURCE_METHODS': ['GET', 'POST'],
    'DOMAIN': DomainConfig({
        'general': ResourceConfig(general),
        'ammountOfGroup': ResourceConfig(ammountOfGroup),
        'rooms': ResourceConfig(rooms),
        'equipment': ResourceConfig(equipment),
        'days': ResourceConfig(days),
        'ranks': ResourceConfig(ranks),
        'groups': ResourceConfig(groups),
        'lessons': ResourceConfig(lessons),
        'existanceOfEquipment': ResourceConfig(existanceOfEquipment),
        'numberOfWeek': ResourceConfig(numberOfWeek),
        'teachers': ResourceConfig(teachers),
        'time': ResourceConfig(time),
        'typesOfRooms': ResourceConfig(typesOfRooms),
        'weeks': ResourceConfig(weeks),
        'prikazy': ResourceConfig(prikazy)
    }).render()
}


app = Eve(auth=None, settings=SETTINGS, data=SQL)

# bind SQLAlchemy
db = app.data.driver
Base.metadata.create_all(engine)
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()


# # using reloader will destroy in-memory sqlite db
app.run(debug=True, use_reloader=False)
