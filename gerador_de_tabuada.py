#Criação de tabuada

numero = int(input("Digite um numero a seu desejo: "))

for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")