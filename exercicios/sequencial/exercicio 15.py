salario_hora = float(input("quantos reais voce ganha por hora? "))
horas_trabalhadas = float(input("quantas horas voce trabalhou no mes? "))

salario_t = salario_hora*horas_trabalhadas
imposto_de_renda = (salario_t*11)/100
inss = (salario_t*8)/100
sindicato = (salario_t*5)/100
valor_liquido = salario_t-imposto_de_renda-inss-sindicato

print("salário bruto",salario_t," reais." " pago ao imposto de renda",imposto_de_renda," reais." " pago ao inss",inss," reais." " pago ao sindicato",sindicato," reais." " valor liquido",valor_liquido," reais.")