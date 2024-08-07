# ♚ LASKERBOT

### O  LASKERBOT é um projeto que usa os recursos das api's do DIALOGFLOW ES e LICHESS. O LASKERBOT dá dicas de como evoluir no Xadrez, além de analisar partidas com notações no formato PGN.  


> [!NOTE]  
> As informações da API utilizada podem ser encontradas no link: https://cloud.google.com/dialogflow/es/docs/quick/api

---

## ♟️ Objetivo
![bot](assets/bot.png)
<h3>O principal objetivo do ChessBot é interagir com o usuário dando dicas de como evoluir no Xadrez. Explanar bases de dados com partidas de Grandes Mestres e/ou partidas clássicas de outrora, recomendar livros de acordo com o nível do enxadrista, além de serviços de análises de partidas.</h3>

> [!TIP]
> O fluxo de conversa do bot leva em conta o nível de cada usuário de acordo com a autoavaliação do próprio usuário, portanto, dependendo do que foi dito por ele no ínicio da conversa, o bot poderá recomendar conteúdos diferentes e ter uma linguagem mais técnica. 

</div>

## Endpoints
<details><summary>Rota GET /</summary>

- Resposta esperada:

    ```json 
        {

         "LaskerBot is Live"

        }
    ``` 

</details>

----
<details><summary>Rota POST /dialogflow</summary>

- Modelo de requisição:

    ```json 
        {

         "mensagem":"oi"

        }
    ``` 
- Resposta esperada:

    ```json 
        {
          "resposta_do_bot" : "Olá, enxadrista!♟️/nSeja bem-vindo! 
           Eu sou o ChessBot./nE você, como se chama?♖♝♘♟️♕"
        }
    ``` 

</details>

## Fluxo de conversa

https://github.com/user-attachments/assets/fb02bbe5-f08f-40b9-a92c-8a48299dca1a

## Exemplo de FALLBACK  

https://github.com/user-attachments/assets/716d6625-2383-40b0-8dda-6ed75f4b2e57

> [!NOTE]
> Como visto no exemplo acima, qualquer assunto fora do contexto do bot levará o usuário à intent de Fallback e só irá voltar ao fluxo de conversa no momento que o usuário inserir algo que esteja no escopo de entendimento do bot.

## Frontend

> [!NOTE]
> O Frontend do LaskerBot está em desenvolvimento no repositório: https://github.com/imrooteodoro/laskerbot-frontend

## ♞ Requisitos

## 🏛️ Arquitetura


[](assets/LaskerBot.svg)


## 🛠️ Tecnologias

<div align="center">
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png" alt="Flask" title="Flask"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183911547-990692bc-8411-4878-99a0-43506cdb69cf.png" alt="GCP" title="GCP"/></code>
</div>

## 🤖 Usar com o seu próprio Agente



## 💻 Desenvolvedor
