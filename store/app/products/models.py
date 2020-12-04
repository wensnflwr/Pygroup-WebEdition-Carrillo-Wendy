from flask import Blueprint

prod = Blueprint('prod', __name__, url_prefix = '/prod')

@prod.route('/')
def products():
  return "Bienvenido a la página de productos"


