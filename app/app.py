from flask import Flask, render_template,request, url_for, redirect
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.before_request
def before_request():
    print('antes de la peticion')

@app.after_request
def after_request(response):
    print('Despues de la peticion')
    return response
    
@app.route('/')
def index():
    cursos = ['Aritmetica', 'Algebra', 'Geometria', 'Calculo']
    data = {
    
        'titulo' : 'Index',
        'bienvenida' : 'Saludos',
        'cursos' : cursos ,
        'numero_cursos' : len(cursos)
    }
    return render_template('index.html', data = data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo' : 'contacto',
        'nombre' : nombre,
        'edad' : edad
    }
    return render_template('contacto.html', data = data)

def query_string():
    print(request)
    print(request.args.get('param_one'))
    print(request.args.get('param_two'))                    
    return 'OK'    

def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func= query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
