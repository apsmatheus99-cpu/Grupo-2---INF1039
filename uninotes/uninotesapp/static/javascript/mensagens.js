const conversas = document.querySelectorAll(".conversa");
const chat = document.querySelector(".chat-mensagens");
const campoTexto = document.querySelector(".campo-mensagem input");
const botaoEnviar = document.querySelector(".campo-mensagem button");

const nomeUsuario = document.querySelector(".chat-cabecalho h3");
const avatar = document.querySelector(".chat-cabecalho .avatar")

const historico_conversa=[
    [
        { texto: "Oi! Você tem o resumo da última aula?", tipo: "recebida" },
        { texto: "Oi, tenho sim! Vou te mandar.", tipo: "enviada" },
        { texto: "Obrigada pelo material!", tipo: "recebida" }
    ],
    [
        { texto: "Oi, Matheus!", tipo: "enviada" },
        { texto: "Você tem os slides da aula?", tipo: "enviada" }
    ],
        [
        { texto: "Oi, Ana!", tipo: "enviada" },
        { texto: "Você foi na aula de hoje?", tipo: "enviada" },
        {texto: "Sim", tipo:"recebida"},
        {texto: "Vou te enviar a lista", tipo: "recebida"}
    ],
    [
        { texto: "Oi, André!", tipo: "enviada" },
        { texto: "Você vai para a monitoria amanhã?", tipo: "enviada" },
        { texto: "Oi! Vou sim", tipo: "recebida"},
        { texto: "Até amanhã!", tipo: "enviada"}
    ],
    [
        {texto: "OIII", tipo:"enviada"},
        {texto: "Tchau", tipo:"recebida"}
    ]
];

let conversaAtual=0; //indice

const campoBusca = document.querySelector(".buscar-conversa");


// funcao de enviar
function enviarMensagem(){
    const mensagem = campoTexto.value.trim();
    if (mensagem!==""){
        historico_conversa[conversaAtual].push({
            texto: mensagem,
            tipo: "enviada"
        });

        const ultimaMensagem = conversas[conversaAtual].querySelector(".dados-conversa p");
        

        const balao = document.createElement("div");
        chat.appendChild(balao);
        balao.textContent=mensagem;
        balao.classList.add("mensagem","enviada")

        ultimaMensagem.textContent= mensagem;
        
        campoTexto.value="";
        
        
    }
}

function mostraConversa(){
    chat.innerHTML="";
    historico_conversa[conversaAtual].forEach(function(mensagem){
        const balao = document.createElement("div");
        chat.appendChild(balao);
        balao.textContent=mensagem.texto;
        balao.classList.add("mensagem",mensagem.tipo)
    })
}



// enviar com botao
botaoEnviar.addEventListener("click",function(){
    enviarMensagem();
});

// enviar com enter
campoTexto.addEventListener("keydown",function(evento){
    if (evento.key == "Enter"){
        enviarMensagem();
    }

})

conversas.forEach(function(conversa,indice){
    conversa.addEventListener("click",function(){
        conversaAtual=indice;

        conversas.forEach(function(conversa_lateral){
            conversa_lateral.classList.remove("selecionada");
        })

        conversa.classList.add("selecionada");

        nomeUsuario.textContent=conversa.querySelector("h4").textContent;
        avatar.textContent=conversa.querySelector(".avatar").textContent;
        mostraConversa();
        
       
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
mostraConversa();