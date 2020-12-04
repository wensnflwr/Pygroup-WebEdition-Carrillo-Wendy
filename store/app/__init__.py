from flask import Flask, Response
from products.models import prod

from store.app.products import views 
from store.app.products.views import products 
app.register_blueprint(prod)
  
ACTIVE_BLUEPRINTS = [('/prod',prod)]

def createapp(config = DevelopmentConfig):
  
  app = Flask(__name__) 
  
  db.init_app(app)
  ma.init_app(app)


  with app.app_context():
    db.create_all()

  for url, blueprint in ACTIVE_BLUEPRINTS:
    app.register_blueprint(blueprint, url_prefix = url) 

@app.route('/')
def start():
  return 'Hello there !'

@app.route(('/<name>/').lower(), methods = ['GET']) 
def user(name): 
  if name == "pygroup": 
    return Response("ERROR! No se puede usar el nombre pygroup", status = 400)
    
  else: 
    return Response("Felicitaciones! Trabajo exitoso {}".format(name), status = 200)
    

if __name__ == "__main__": 
  app_flask = createapp()

#from store.app.products import views 
#from store.app.products.views import products 
app.register_blueprint(prod)
  
if __name__ == "__main__": 

  app.run('0.0.0.0', port = 8080)

