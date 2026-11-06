
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
@app.route('/welcome/<name>')
def welcome2(name=None):
    return render_template('person2.html', name=name)

@app.route('/welcome/<first_name>/<last_name>')
def welcome3(first_name, last_name):
    return render_template(
        'person2.html',
        name=f'{first_name} {last_name}'
    )

@app.route('/list')
def welcome4():
    names = ['Jane', 'John', 'Alice', 'Bob']
    return render_template('list.html', names=names)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return render_template(
        'multiply.html',
        a=a,
        b=b,
        result=result
    )

if __name__ == '__main__':
    app.run(debug=True)
