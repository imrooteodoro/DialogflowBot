document.addEventListener("DOMContentLoaded", () => {
    const historicoMensagens = document.getElementById(
        "historico-de-mensagens"
    );
    historicoMensagens.scrollTop = historicoMensagens.scrollHeight;

    const formMensagem = document.getElementById("form-mensagem");
    formMensagem.addEventListener("submit", (event) => {
        event.preventDefault();
        const mensagem = document.getElementById("mensagem").value;

        fetch("/dialogflow", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                mensagem: mensagem,
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                historicoMensagens.innerHTML += `
    <li><strong>Você:</strong> ${mensagem}</li>
    ${data.resposta_do_bot.includes("<img")
                        ? `<li><strong>Bot:</strong> ${data.resposta_do_bot}</li>`
                        : `<li><strong>Bot:</strong> ${data.resposta_do_bot}</li>`
                    }
  `;
                document.getElementById("mensagem").value = "";

                // Role para a última mensagem
                historicoMensagens.scrollTop = historicoMensagens.scrollHeight;
            });
    });
});