
#email e senha antecipados
email_cadastrado = "usuario@email.com"
senha_cadastrada = "senha123"

# Solicite ao usuário email e senha
while True:
    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")

    # Verifique se o email e senha são iguais
    if email_usuario == email_cadastrado and senha_usuario == senha_cadastrada:
        print("Login bem-sucedido!")
        break
    else:
        print("Email ou senha incorretos. Tente novamente.")