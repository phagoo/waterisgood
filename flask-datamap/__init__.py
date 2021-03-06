
from flask import Flask, render_template
from flask import url_for
from functools import wraps
from flask import request, Response
import os
from flask import redirect
from werkzeug import secure_filename
from flask import send_from_directory

app = Flask(__name__)

@app.route('/introduction_kpe')
def introduction():
    try:
        return render_template("Introduction.html")
    except Exception as e:
        return str(e)


@app.route('/bangladesh')
def bangladesh():
    try:
        return render_template("bangladesh2.htm")
    except Exception as e:
        return str(e)


@app.route('/singapore')
def singapore():
    try:
        return render_template("singapore2.html")
    except Exception as e:
        return str(e)

@app.route('/saopaulo')
def saopaulo():
    try:
        return render_template("saopaulo.html")
    except Exception as e:
        return str(e)

@app.route('/israel')
def israel():
    try:
        return render_template("israel.html")
    except Exception as e:
        return str(e)


@app.route('/another')
def another():
    try:
        return render_template("indexClickAndSlide.html")
    except Exception as e:
        return str(e)

@app.route('/')
def main():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)

