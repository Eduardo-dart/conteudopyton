limite_de_peso = 50
pegou = float(input("quantos kilos joão pegou? "))

if pegou > limite_de_peso:
    exedente = pegou - limite_de_peso
    multa = exedente * 4
    print("João pegou", exedente, "kg a cima do permitido, ele terá que pagar", multa, "reais de multa")
else:
    print("não foi maior do que o permitido")