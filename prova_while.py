# Inicializa as variáveis
soma = 0
quantidade_numeros = 0

# Loop para ler os números do teclado
while True:
    # Solicita ao usuário inserir um número
    numero = int(input("Digite um número (digite 0 para sair): "))

    # Verifica se o usuário digitou 0 para sair do loop
    if numero == 0:
        ("Você decidiu sair do programa")
        break

    # Adiciona o número à soma e incrementa a quantidade de números
    soma += numero
    quantidade_numeros += 1

# Verifica se foram digitados números antes de calcular a média
if quantidade_numeros > 0:
    media = (soma / quantidade_numeros)
    media_formatada = "{:.2f}".format(media)
    print(f"\nQuantidade de números digitados: {quantidade_numeros}")
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media_formatada}")
else:
    print("Nenhum número foi digitado.")
