# wsgi.py
# pylint: disable=missing-docstring
from flask import Flask, render_template, request, session
from flask_session import Session
from game import Game

APP = Flask(__name__)
SESSION_TYPE = 'filesystem'
APP.config.from_object(__name__)
Session(APP)

@APP.route('/')
def home():
    game = Game()
    if 'score' not in session:
        session['score'] = 0
    return render_template('home.html', grid=game.grid, score=session['score'])

@APP.route('/check', methods=["POST"])
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
