#Flask permite usar plantillas para el contenido dinámico de páginas web.

#Para usar este se puede usar el método "render_template()". Lo único que se debe hacer es proveer el nombre de la plantilla y las variables que se vayan a pasar al mecanismo de plantillas

#Ejemplo:

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#Enlaces de busqueda:

#https://riptutorial.com/es/flask/example/5303/uso-de-render-template
#https://flask.palletsprojects.com/en/1.1.x/quickstart/
