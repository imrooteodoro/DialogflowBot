import os
from google.oauth2 import service_account
import google.auth.transport.requests
import requests

def get_access_token():
    # Carrega as credenciais do arquivo JSON
    service_path = '/home/teodoro/Documents/chatbots/src/ok.json'
    creds = service_account.Credentials.from_service_account_file(service_path,  
        scopes=['https://www.googleapis.com/auth/dialogflow']
    )

    # Crie um objeto de solicitação de autenticação
    auth_req = google.auth.transport.requests.Request()

    # Atualize as credenciais
    creds.refresh(auth_req)

    # Obtenha o token de acesso
    access_token = creds.token

    return access_token