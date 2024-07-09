from flask import Flask, request, jsonify, render_template
from services.gcp_auth.auth import get_access_token
from services.payload import send_message_to_dialogflow
from utils.generate_id import session_id
from models.messages.bot_message import extract_bot_response

import re

historico_de_mensagens = []
user_id = session_id()

def botget(app):
    @app.route('/', methods=['GET'])
    def get_mensagem_do_bot():
        global user_id
        user_id = session_id()  # Gera um único user_id para cada requisição get
        global historico_de_mensagens
        historico_de_mensagens.clear()
        return render_template('index.html', historico_de_mensagens=historico_de_mensagens)

def botpost(app):
    @app.route('/dialogflow', methods=['POST'])
    def enviar_mensagem_para_dialogflow():
        global historico_de_mensagens
        try:
            mensagem = request.json.get('mensagem')
            access_token = get_access_token()
            resultado = send_message_to_dialogflow(mensagem, access_token,user_id)
            resposta_do_bot = extract_bot_response(resultado)
            return jsonify({'resposta_do_bot': resposta_do_bot})
        except Exception as e:
            return jsonify({'error': 'Internal Server Error:' + str(e)}), 500
    


    