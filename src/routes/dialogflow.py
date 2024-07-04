import requests
from flask import Flask, request, jsonify, app, render_template
import subprocess
from auth.auth import get_access_token
from services.payload import send_message_to_dialogflow
from services.payload import user_id
from utils.generate_id import session_id
import re


historico_de_mensagens = []
def botpost(app):
    @app.route('/dialogflow', methods=['POST'])
    def enviar_mensagem_para_dialogflow():
        global historico_de_mensagens
        mensagem = request.json.get('mensagem')
        access_token = get_access_token()
        resultado = send_message_to_dialogflow(mensagem, access_token)
        
        if "queryResult" in resultado and "fulfillmentMessages" in resultado["queryResult"]:
            fulfillment_message = resultado["queryResult"]["fulfillmentMessages"][0]
            if "text" in fulfillment_message and "text" in fulfillment_message["text"]:
                resposta_do_bot = fulfillment_message["text"]["text"][0]
                urls = re.findall(r'(https?://\S+)', resposta_do_bot)
                for url in urls:
        # Formato de url
                   link = f'<a href="{url}">{url}</a>'
        # Retorna a url em formato de url
                   resposta_do_bot = resposta_do_bot.replace(url, link)
                   historico_de_mensagens.append({"usuario": mensagem, "bot": resposta_do_bot})
            
            else:
                resposta_do_bot = "Sorry, I didn't understand that."
                historico_de_mensagens.append({"usuario": mensagem, "bot": resposta_do_bot})
        else:
            resposta_do_bot = "Sorry, I didn't understand that."
            historico_de_mensagens.append({"usuario": mensagem, "bot": resposta_do_bot})
        
        return jsonify({'resposta_do_bot': resposta_do_bot})

def botget(app):
    @app.route('/', methods=['GET'])
    def get_mensagem_do_bot():
        user_id = session_id()
        global historico_de_mensagens
        return render_template('index.html', historico_de_mensagens = historico_de_mensagens)
    
