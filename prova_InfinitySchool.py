##Prova sobre condicionais

#Questão 01
"""
[LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro. 
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.
"""

velocidade_carro = float(input("Digite a velocidade do carro em km/h: "))
limite_velocidade = 80
#Declara o valor da multa
valor_da_multa = 20

if velocidade_carro > limite_velocidade:
    # Calcula a multa
    multa = (velocidade_carro - limite_velocidade) * valor_da_multa

    print(f"Você foi multado! Velocidade acima do limite permitido de {limite_velocidade} km/h.")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade. Dirija com segurança!")
