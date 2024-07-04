from flask import Flask, request, jsonify
import requests
import subprocess
from routes.dialogflow import botpost, botget

app = Flask(__name__, static_folder='public')

botpost(app)
botget(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
