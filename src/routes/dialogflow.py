from flask import Flask, request, jsonify, render_template
from auth.auth import get_access_token
from services.payload import send_message_to_dialogflow
from utils.generate_id import session_id
import re

historico_de_mensagens = []
user_id = session_id()  

def botget(app):
    @app.route('/', methods=['GET'])
    def get_mensagem_do_bot():
        user_id_get = session_id()  # Gera um único user_id para cada requisição get
        global historico_de_mensagens
        return render_template('index.html', historico_de_mensagens=historico_de_mensagens)

def botpost(app):
    @app.route('/dialogflow', methods=['POST'])
    def enviar_mensagem_para_dialogflow():
        global historico_de_mensagens
        mensagem = request.json.get('mensagem')
        access_token = get_access_token()
        resultado = send_message_to_dialogflow(mensagem, access_token, user_id)

        if "queryResult" in resultado and "fulfillmentMessages" in resultado["queryResult"]:
            fulfillment_message = resultado["queryResult"]["fulfillmentMessages"][0]
            if "text" in fulfillment_message and "text" in fulfillment_message["text"]:
                resposta_do_bot = fulfillment_message["text"]["text"][0]
                resposta_do_bot = resposta_do_bot.replace('\n', '<br>')
                urls = re.findall(r'(https?://\S+)', resposta_do_bot)
                for url in urls:
                    link = f'<a href="{url}">{url}</a>'
                    resposta_do_bot = resposta_do_bot.replace(url, link)
                    historico_de_mensagens.append({"usuario": mensagem, "bot": resposta_do_bot})

            else:
                resposta_do_bot = "Sorry, I didn't understand that."
                historico_de_mensagens.append({"usuario": mensagem, "bot": resposta_do_bot})
        else:
            resposta_do_bot = "Sorry, I didn't understand that."
            historico_de_mensagens.append({"usuario": mensagem, "bot": resposta_do_bot})

        return jsonify({'resposta_do_bot': resposta_do_bot})