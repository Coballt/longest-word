# wsgi.py
from flask import Flask, render_template, request, session
from flask_session import Session
from game import Game

app = Flask(__name__)
SESSION_TYPE='filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    game = Game()
    if 'score' not in session:
        session['score'] = 0
    return render_template('home.html', grid=game.grid, score=session['score'])

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    if is_valid:
        if 'score' in session:
            session['score'] += Game.return_score(word)
        else:
            session['score'] = 0
    return render_template('check.html',
        is_valid=is_valid,
        grid=game.grid,
        word=word,
        score=session['score'])


@app.route('/get/')
def get():
    return session.get('key', 'not set')
