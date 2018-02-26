import falcon
from wsgiref import simple_server

class HereHome(object) :
    def on_get(self , req , res):
        res.body = ('Hey barr , this is donald \n')

class tempRoute(object):
    def on_get(self , req , res , temp , time):
        res.body = (temp , ' degrees at ', time , ' IST')

root = HereHome() 
temp = tempRoute()

app = falcon.API()

app.add_route('/' , root)
app.add_route('/{temp}/{time}/ok' , temp)

if __name__ == '__main__':
    http = simple_server.make_server( '127.0.0.1' , 8000 , app )
    http.serve_forever()