numero1 = float(input("digite o primeiro numero"))
numero2 = float(input("digite o segundo numero"))
numero3 = float(input("digite o terceiro numero"))
if numero1>numero2 and numero1>numero3:
    print("o maior numero é o:" ,numero1,"(primeiro numero)")
elif numero2>numero1 and numero2>numero3:
    print("o maior numereo é o:",numero2,"(segundo numero)")
elif numero3>numero1 and numero3>numero2:
    print("o maior numero é o:",numero3,"(terceiro numero)")
else:
    print("os numeros sao iguais")