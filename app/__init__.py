from flask import Flask, render_template
from mongoengine import connect, Document, StringField


app = Flask(__name__)

app.config.from_object('config.Development')

connect('devRadar', host=app.config['DATABASE_URL'])


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
