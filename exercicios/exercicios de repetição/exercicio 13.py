valor = int(input("digite um valor: "))

contador = valor
resultado = 1
while contador>0:
    resultado = resultado * contador
    contador = contador - 1

print(f"o fatorial de {valor} é {resultado}")