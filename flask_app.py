
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/') #Path at the back of the domain name
def hello_world():
    return 'Hello, this is Pantakan Bunleang (Nawin).'

@app.route('/apple') #when there is path /apple at the back of the domain name, this method will be executed.
def hello_apple():
    return 'Thisssss is apple page in the flask webapp.'

@app.route('/today')
def today():
    return str(date.today())

@app.route('/hi')
def hi():
    return 'hi'
