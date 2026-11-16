const conversas = document.querySelectorAll(".conversa");
const campoDestinatario = document.querySelector("#destinatario");
const nomeUsuario = document.querySelector(".chat-cabecalho h3");
const avatar = document.querySelector(".chat-cabecalho .avatar");
const campoBusca = document.querySelector(".buscar-conversa");
const botaoEnviar = document.querySelector("#botao-enviar");




conversas.forEach(function(conversa,indice){
    conversa.addEventListener("click",function(){

        conversas.forEach(function(conversa_lateral){
            conversa_lateral.classList.remove("selecionada");
        })

        conversa.classList.add("selecionada");
        campoDestinatario.value=conversa.dataset.userId;
        botaoEnviar.disabled=false;

        nomeUsuario.textContent=conversa.querySelector("h4").textContent;
        avatar.textContent=conversa.querySelector(".avatar").textContent;
        window.location.href= "?contato="+ conversa.dataset.userId;
    })
})

//buscar conversa pelo nome do usuario
campoBusca.addEventListener("input", function(){
    const pesquisa = campoBusca.value.toLowerCase();

    conversas.forEach(function(conversa){
        const nome= conversa.querySelector("h4").textContent.toLowerCase();
        
        if (nome.includes(pesquisa)){
            conversa.style.display = "flex";
        }
        else{
            conversa.style.display = "none";
        }
        
    })

})
