document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("form-comentario");
    const campoComentario = document.getElementById("campo-comentario");
    const listaComentarios = document.getElementById("lista-comentarios");
    const nomeUsuario = listaComentarios.dataset.usuario;

    formulario.addEventListener("submit", function (event) {
        event.preventDefault();

        const texto = campoComentario.value.trim();

        if (texto === "") {
        alert("Digite um comentário antes de publicar.");
        return;
        }

        const comentario = document.createElement("div");
        comentario.classList.add("comentario");

        const autor = document.createElement("p");
        autor.classList.add("autor-comentario");
        autor.textContent = nomeUsuario;

        const mensagem = document.createElement("p");
        mensagem.classList.add("texto-comentario");
        mensagem.textContent = texto;

        const botaoExcluir = document.createElement("button");
        botaoExcluir.textContent = "Excluir";
        botaoExcluir.classList.add("excluir-comentario");

        botaoExcluir.addEventListener("click", function () {
            comentario.remove();
        });

        comentario.appendChild(autor);
        comentario.appendChild(mensagem);
        comentario.appendChild(botaoExcluir);

        listaComentarios.appendChild(comentario);
        campoComentario.value = "";
    });
});