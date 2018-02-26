from flask import Flask
import dbManager 


app = Flask(__name__)

@app.route('/')
def home():
    return 'This is root'

@app.route('/user/<name>')
def user(name):
    return 'Hi %s'%name

@app.route('/push/<deviceName>/<temprature>')
def storeTemprature(deviceName , temprature ):
    data = {'deviceName' : deviceName , 'value': temprature }
    dbManager.insertInDevice(data)
    return "{} {} saved in edge".format(deviceName , temprature )


@app.route('/get/temprature/mean/<deviceName>')
def getMean(deviceName):
    mean = dbManager.getAvg(deviceName)
    return "{} mean is {} ".format(deviceName , mean)    

@app.route('/push/<deviceName>/<Gx>/<Gy>/<Gz>')
def storeGyro(deviceName , Gx , Gy ,Gz):
    data = {'deviceName' : deviceName , 'Gx': Gx , 'Gy' : Gy , 'Gz' : Gz }
    dbManager.insertGyroData(data)
    return "{} {} {} {} saved in edge".format(deviceName , Gx , Gy , Gz )

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')