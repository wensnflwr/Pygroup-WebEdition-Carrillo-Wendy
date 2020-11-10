from flask import Flask

app = Flask(__name__) 

@app.route(('/<string:name>'), methods = ['GET']) 
def index(name): 
  if one == "pygroup": 
    return Response("ERROR! No se puede usar el nombre pygroup", status = 400) 
  return  Response("Felicitaciones! Trabajo exitoso {}".format(name), status = 200) 

#from store.app.products import views 
#from store.app.products.views import products 
  
if __name__ == "__main__": 
  app.run(bug = True)