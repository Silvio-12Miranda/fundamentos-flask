from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cursos = ['Aritmetica', 'Algebra', 'Geometria', 'Calculo']
    data = {
    
        'titulo' : 'Index',
        'Bienvenida' : 'Saludos',
        'cursos' : cursos ,
        'Numero de cursos' : len(cursos)
    }
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run()
