from flask import render_template, url_for
from app import app
from collections import namedtuple

Link = namedtuple('Link', ['link', 'display'])

@app.route('/')
@app.route('/index')
def index():
    links = []
    return render_template('index.html', links=links, central_image="static/gen3.png")

@app.route('/')
@app.route('/mood_rings')
def mood_rings():
    links = []
    return render_template('mood_rings.html', links=links, central_image="static/ch2.png")

@app.route('/')
@app.route('/movie_rugs')
def movie_rugs():
    links = []
    return render_template('movie_rugs.html', links=links, central_image="static/rugroyal.png")

@app.route('/')
@app.route('/visual_vinyls')
def visual_vinyls():
    links = []
    return render_template('visual_vinyls.html', links=links, central_image="static/vvsomething.png")

@app.route('/')
@app.route('/evolution')
def evolution():
    links = []
    return render_template('evolution.html', links=links, central_image="static/evo1.png")

@app.route('/contact')
def contact():
    links = []
    return render_template('contact.html', links=links)