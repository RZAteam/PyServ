from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.automap import automap_base

Base = declarative_base()


class CommonColumns(Base):
    __abstract__ = True
    _created = Column(DateTime, default=func.now())
    _updated = Column(DateTime, default=func.now(), onupdate=func.now())
    _etag = Column(String(40))


class general(CommonColumns):
    __tablename__ = "t_general"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_zapisi = Column(Integer(), primary_key=True)
    id_prep = Column(Integer(),ForeignKey('t_prep.id_prep'), nullable=False)
    id_grup = Column(Integer(),ForeignKey('t_gr.id_grup'), nullable=False)
    id_time = Column(Integer(),ForeignKey('t_time.id_time'), nullable=False)
    id_week = Column(Integer(),ForeignKey('t_number_of_week.id_week'), nullable=False)
    id_day = Column(Integer(),ForeignKey('t_day.id_day'), nullable=False)
    id_name_lesson = Column(Integer(),ForeignKey('t_lesson.id_name_lesson'), nullable=False)
    id_kolvo_grup = Column(Integer(),ForeignKey('t_kolvo_grup.id_kolvo_grup'), nullable=False)
    id_aud = Column(Integer(), ForeignKey('t_aud.id_aud'), nullable=False)


class ammountOfGroup(CommonColumns):
    __tablename__ = "t_kolvo_grup"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_kolvo_grup = Column(Integer(), primary_key=True)
    grup = Column(String(255), nullable=False)


class rooms(CommonColumns):
    __tablename__ = "t_aud"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_aud = Column(Integer(), primary_key=True)
    aud_number = Column(String(255), nullable=False)
    id_type_aud = Column(Integer(), ForeignKey('t_type_aud.id_type_aud'), nullable=False)


class equipment(CommonColumns):
    __tablename__ = "t_equip_aud"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_equip = Column(Integer(), primary_key=True)
    equip = Column(String(255), nullable=False)


class days(CommonColumns):
    __tablename__ = "t_day"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_day = Column(Integer(), primary_key=True)
    name_day = Column(String(255), nullable=False)


class ranks(CommonColumns):
    __tablename__ = "t_dol"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_dolg = Column(Integer(), primary_key=True)
    dolg = Column(String(255), nullable=False)


class existanceOfEquipment(CommonColumns):
    __tablename__ = "t_aud_equip"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_a_e = Column(Integer(), primary_key=True)
    id_aud = Column(Integer(), ForeignKey('t_aud.id_aud'), nullable=False)
    id_equip = Column(Integer(), ForeignKey('t_equip_aud.id_equip'), nullable=False)
    kolvo = Column(Integer(), nullable=False)


class groups(CommonColumns):
    __tablename__ = "t_gr"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_grup = Column(Integer(), primary_key=True)
    Number = Column(String(255), nullable=False)


class lessons(CommonColumns):
    __tablename__ = "t_lesson"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_name_lesson = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    # weeks = relationship("weeks", back_populates="lessons")
    id_t_week = Column(Integer(), ForeignKey('t_week.id_week'), nullable=False)
    # ForeignKeyConstraint(['id_t_week'], ['t_week.id_week'], name='t_lesson_c1')


class numberOfWeek(CommonColumns):
    __tablename__ = "t_number_of_week"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_week = Column(Integer(), primary_key=True)
    num_week = Column(String(255), nullable=False)


class teachers(CommonColumns):
    __tablename__ = "t_prep"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_prep = Column(Integer(), primary_key=True)
    FIO = Column(String(255), nullable=False)
    id_dolg = Column(Integer(), ForeignKey('t_dol.id_dolg'), nullable=False)
    # ForeignKeyConstraint(['id_dolg'], ['testRasp.t_dol.id_dolg'], name='t_prep_c1')


class time(CommonColumns):
    __tablename__ = "t_time"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_time = Column(Integer(), primary_key=True)
    time = Column(String(255), nullable=False)


class typesOfRooms(CommonColumns):
    __tablename__ = "t_type_aud"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_type_aud = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)


class weeks(CommonColumns):
    __tablename__ = "t_week"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_week = Column('id_week', Integer(), primary_key=True)
    week = Column(String(255), nullable=False)
    # lessons = relationship("lessons", back_populates="weeks")


class prikazy(CommonColumns):
    __tablename__ = "t_prikazy"
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'UTF8MB4'}
    id_img = Column('id_img', Integer(), primary_key=True, autoincrement=True)
    src = Column(String(255), nullable=False)
