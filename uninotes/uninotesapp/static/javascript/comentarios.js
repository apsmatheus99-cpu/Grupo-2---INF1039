document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("form-comentario");
    const campoComentario = document.getElementById("campo-comentario");
    const listaComentarios = document.getElementById("lista-comentarios");

    formulario.addEventListener("submit", async function (event) {

        event.preventDefault();

        const texto = campoComentario.value.trim();

        if (texto === "") {
            alert("Digite um comentário antes de publicar.");
            return;
        }

        try {

            const resposta = await fetch(formulario.action, {
                method: "POST",
                body: new FormData(formulario)
            });

            const dados = await resposta.json();

            if (!resposta.ok) {
                alert(dados.erro || "Não foi possível publicar o comentário.");
                return;
            }

            const comentario = document.createElement("div");
            comentario.classList.add("comentario");

            const autor = document.createElement("p");
            autor.classList.add("autor-comentario");
            autor.textContent = dados.usuario;

            const mensagem = document.createElement("p");
            mensagem.classList.add("texto-comentario");
            mensagem.textContent = dados.texto;

            comentario.appendChild(autor);
            comentario.appendChild(mensagem);

            listaComentarios.appendChild(comentario);

            campoComentario.value = "";

        } catch (erro) {

            console.error("Erro:", erro);
            alert("Erro ao enviar o comentário.");

        }

    });

});