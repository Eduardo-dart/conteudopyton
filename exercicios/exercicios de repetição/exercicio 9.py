numero = int(input("digite o valor do numero para fazer a tabuada"))
while numero< 0 or numero > 10:
    print(" valor inválido")
    numero = int(input("digite o valor do numero para fazer a tabuad"))

for multiplicador in range(0,11):
    resultado = numero* multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")