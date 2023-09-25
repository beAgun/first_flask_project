from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(width=10, height=5)
    return render_template('index.html')

@app.route('/life')
def life():
    a = GameOfLife()
    if a.counter > 0:
        a.form_new_generation()
    a.counter += 1
    return render_template('life.html', a=a)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)