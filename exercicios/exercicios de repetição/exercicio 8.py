numero1 = int(input("digite um numero"))
numero2 = int(input(" digite outro numero"))
soma = 0
for numero in range(numero1+1,numero2):
    print(numero, end= " ")
    soma = soma + numero

print(f"a soma é {soma}")