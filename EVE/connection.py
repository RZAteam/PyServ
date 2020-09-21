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
# from Tables import general, Base, ammountOfGroup, rooms, equipment, days, ranks, existanceOfEquipment, groups, lessons, numberOfWeek, teachers, time, typesOfRooms, weeks

pymysql.install_as_MySQLdb()
# sqlalchemy.__version__
engine = sqlalchemy.create_engine('mysql://user:passwrd@localhost/RZAPlatform', echo=True)
# engine.connect()
# # engine.execute("CREATE DATABASE testRasp")
# engine.execute("USE testRasp")  # select new db
# metadata = MetaData()

# metadata.reflect(engine)

# Table('t_general', metadata,Integer(),
#       Column('_created', DateTime, default=func.now()),
#       Column('_updated', DateTime, default=func.now(), onupdate=func.now()),
#       Column('_etag', String(40)), extend_existing=True)

# Base = automap_base(metadata=metadata)
# Base.prepare()

Base = automap_base()
Base.prepare(engine, reflect=True)

general = Base.classes.t_general
ammountOfGroup = Base.classes.t_kolvo_grup
rooms = Base.classes.t_aud
equipment = Base.classes.t_equip_aud
days = Base.classes.t_day
ranks = Base.classes.t_dol
existanceOfEquipment = Base.classes.t_aud_equip
groups = Base.classes.t_gr
lessons = Base.classes.t_lesson
numberOfWeek = Base.classes.t_number_of_week
teachers = Base.classes.t_prep
time = Base.classes.t_time
typesOfRooms = Base.classes.t_type_aud
weeks = Base.classes.t_week


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
    }).render()
}


# class TokenAuth(TokenAuth):
#     def check_auth(self, token, allowed_roles, resource, method):
#         """First we are verifying if the token is valid. Next
#         we are checking if user is authorized for given roles.
#         """
#         login = User.verify_auth_token(token)
#         if login and allowed_roles:
#             user = app.data.driver.session.query(User).get(login)
#             return user.isAuthorized(allowed_roles)
#         else:
#             return False

# print("Hi")
# # for i in Base.classes:
# #   print(i)
# m = sqlalchemy.MetaData()
# m.reflect(engine)
# print("start")
# for table in m.tables.values():
#     print(table.name)

app = Eve(auth=None, settings=SETTINGS, data=SQL)
# register_views(app)

# bind SQLAlchemy
db = app.data.driver


# for i in Base.metadata.sorted_tables:
#     print(i.foreign_keys)
#     print(i.name)

Base.metadata.create_all(engine)
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

# # using reloader will destroy in-memory sqlite db
app.run(debug=True, use_reloader=False)
