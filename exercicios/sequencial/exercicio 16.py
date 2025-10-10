import math
area = float(input("Informe a area a ser pintada"))

cob_por_metro = 3
qtd_tinta_lata = 18
valor_lata = 80

litros_necessarios = area/cob_por_metro
print("serão necessarios",litros_necessarios,"L de tinta")

qtd_latas = litros_necessarios/qtd_tinta_lata
print("serão necessarios",qtd_latas,"latas de tinta")

print("###com o valor exato###")
valor = qtd_latas*valor_lata
print("O valor necessário de tinta é R$",round(valor,2))

print("### Com quantidade inteiras de latas ###")
qtd_latas += math.ceil(qtd_latas)
print("São necessarios",qtd_latas,"latas de tinta")
valor = qtd_latas*valor_lata
print("O valor necessário da tenta é R$",valor)