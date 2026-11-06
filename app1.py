from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello from Flask!</h1>'

@app.route('/person/<name>')
def welcome1(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/person/<first_name>/<last_name>')
def welcome2(first_name, last_name):
    return f'<h1>Hello, {first_name} {last_name}!</h1>'

@app.route('/square/<int:number>')
def square_evaluation(number):
    square = number * number
    return f'<h1>{number} squared is {square}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
