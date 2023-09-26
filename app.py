from flask import Flask, render_template, request, redirect
from game_of_life import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html', title='Welcome to game life')

@app.route('/index', methods=['post'])
def index():
    width = int(request.form.get('width'))
    height = int(request.form.get('height'))
    GameOfLife(width=width, height=height)
    return render_template('index.html')

@app.route('/dynamic_life', methods=['get', 'post'])
def dynamic_life():
    a = GameOfLife()
    if a.counter > 0:
        a.form_new_generation()
    a.counter += 1
    return render_template('dynamic_life.html', a=a)


@app.route('/life')
def life():
    a = GameOfLife()
    return render_template('life.html', a=a)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)