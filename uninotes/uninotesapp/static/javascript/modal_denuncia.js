(function () {
    const modal = document.getElementById("modal-denuncia");
    const abrir = document.getElementById("abrir-modal-denuncia");
    const fechar = document.getElementById("fechar-modal-denuncia");

    if (!modal || !abrir || !fechar) {
        console.error("Modal ou botão não encontrado.");
        return;
    }

    abrir.addEventListener("click", function (evento) {
        evento.preventDefault();
        modal.classList.add("ativo");
    });

    fechar.addEventListener("click", function () {
        modal.classList.remove("ativo");
    });

    modal.addEventListener("click", function (evento) {
        if (evento.target === modal) {
            modal.classList.remove("ativo");
        }
    });

    document.addEventListener("keydown", function (evento) {
        if (evento.key === "Escape") {
            modal.classList.remove("ativo");
        }
    });
})();
