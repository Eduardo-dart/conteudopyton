nota = float(input("qual a sua nota?"))
while nota < 0 or nota > 10:
    print("valor invalido, digite um valor válido")
    nota = float(input("qual a sua nota?"))