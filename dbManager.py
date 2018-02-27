from sqlalchemy import Column, Integer, String , Float, DateTime ,create_engine , ForeignKey ,insert ,MetaData , Table


def insertInDevice(data):
    dbstring = 'sqlite:///somedb.sqlite'
    engine = create_engine(dbstring)
    conn = engine.connect()
    metadata = MetaData()

    devi = Table('temprature' , metadata , autoload=True , autoload_with = engine)

    ins  = devi.insert().values(deviceName=data['deviceName'] , value=data['value'])
    ins.compile().params

    return conn.execute(ins)



def insertGyroData(data):
    dbstring = 'sqlite:///somedb.sqlite'
    engine = create_engine(dbstring)
    conn = engine.connect()
    metadata = MetaData()

    devi = Table('gyro' , metadata , autoload=True , autoload_with = engine)

    ins  = devi.insert().values(deviceName=data['deviceName'] , Gx=data['Gx'] , Gy=data['Gy'] , Gz=data['Gz'])
    ins.compile().params

    return conn.execute(ins)

def insertGPSData(data):
    dbstring = 'sqlite:///somedb.sqlite'
    engine = create_engine(dbstring)
    conn = engine.connect()
    metadata = MetaData()

    devi = Table('gps' , metadata , autoload=True , autoload_with = engine)

    ins  = devi.insert().values(deviceName=data['deviceName'] , lon=data['lon'] , lat=data['lat'])
    ins.compile().params

    return conn.execute(ins)    


def getAvg(deviceID):
    dbstring = 'sqlite:///somedb.sqlite'
    engine = create_engine(dbstring)
    conn = engine.connect()
    metadata = MetaData()

    sql = "select avg(value) from temprature where deviceName = '{}'".format(deviceID)
 #   print (sql)
    res = conn.execute(sql).fetchall()

    return (res[0][0])


