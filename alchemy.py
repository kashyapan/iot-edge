from sqlalchemy import Column, Integer, String , Float, DateTime ,create_engine , ForeignKey ,insert ,MetaData , Table 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

'''
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
, ForeignKey('device.id')
'''

class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer , primary_key=True)
    deviceType = Column(String)
    deviceName = Column(String)

    def __repr__(self):
        return "{}({} {} {})".format(__tablename__ ,id , deviceType , deviceName)


class Temprature(Base):
    __tablename__ = 'temprature'
    id = Column(Integer , primary_key=True)
    deviceName = Column(String  )
    updated = Column(DateTime, default=func.now())
    value  =Column(Float)

    def __repr__(self):
        return "{}({} {} {} {})".format(__tablename__ ,id , deviceName , updated ,value)

class Gyro(Base):
    __tablename__ = 'gyro'
    id = Column(Integer , primary_key=True)
    deviceName  =Column(String)
    updated = Column(DateTime  ,default=func.now())
    Gx = Column(Float)
    Gy = Column(Float)
    Gz = Column(Float)

    def __repr__(self):
        return "{}({})".format(__tablename__ ,id )

dbstring = 'sqlite:///somedb.sqlite'

engine = create_engine(dbstring)

conn = engine.connect()

Base.metadata.create_all(engine)
print ( engine.table_names() )


'''
#temp = Table('temprature')

metadata = MetaData()

devi = Table('device' , metadata , autoload=True , autoload_with = engine)

ins  = devi.insert().values(deviceType='Arduino' , deviceID='UNO1010')
ins.compile().params


print (ins) 

result = conn.execute(ins)
'''

