$(document).ready(function () {
    $("#contact-form").validate({
        rules: {
            "name": {
                required: true,
                minlength: 5
            },
            "email": {
                required: true,
                email: true
            },
            "subject": {
                required: true,
                minlength: 5
            },
            "message": {
                required: true,
                minlength: 25
            }
        },
        messages: {
            "name": {
                required: "Hm... Nós gostamos de saber o nome dos nossos contatos. Qual o seu?",
                minlength: "Seu nome é curtinho assim mesmo? Que tal preencher com teu sobrenome também?"
            },
            "email": {
                required: "Por favor, informe um e-mail para que possamos te responder...",
                email: "Este e-mail não parece ser válido. Corrige aí, vai!"
            },
            "subject": {
                required: "Que tal nos dizer o assunto da sua mensagem?",
                minlength: "Que tal um assunto mais claro? Este está muito curtinho ainda..."
            },
            "message": {
                required: "Ué... Escreve aí sua mensagem! Nós prometemos ler e responder tudo. :)",
                minlength: "É só isso mesmo? Quanto mais clara a sua mensagem for, mais clara será nossa resposta! "
            }
        }
    });
});