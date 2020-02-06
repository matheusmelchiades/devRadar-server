from flask import Flask, render_template
from mongoengine import connect, Document, StringField

from . import routes

server = Flask(__name__)

server.config.from_object('config.Development')

connect('devRadar', host=server.config['DATABASE_URL'])

from app.components.developers.controller import Controller as DevController

##########
#  DEVS
##########
@server.route('/devs', methods=['GET'])
def getDevs():
    return DevController.getDevs()


@server.errorhandler(404)
def not_found(error):
    return render_template('404.html')

print('CHAMO 1')