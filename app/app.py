from flask import Flask, render_template,request

app = Flask(__name__)

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
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.add_url_rule('/query_string', view_func= query_string)
    app.run()
