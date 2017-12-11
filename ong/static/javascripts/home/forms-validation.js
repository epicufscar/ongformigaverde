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
                required: "Precisamos saber com quem conversamos. Qual o seu nome?",
                minlength: "Este me parece ser um nome curto de mais. Que tal adicionar o sobrenome também?"
            },
            "email": {
                required: "Por favor, informe um e-mail para que possamos te responder...",
                email: "Você deve inserir um e-mail válido, por favor."
            },
            "subject": {
                required: "Que tal nos dizer o assunto da sua mensagem?",
                minlength: "Este assunto parece ser curto demais, tente aumentá-lo."
            },
            "message": {
                required: "É aqui que você deve inserir sua mensagem. Nós prometemos ler e responder tudo.",
                minlength: "É só isso mesmo? Quanto mais clara for sua mensagem, mais clara poderá ser nossa resposta!"
            }
        }
    });
});