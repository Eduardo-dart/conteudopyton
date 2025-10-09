salarioph = float(input("quantos reais voce ganha por hora?"))
horastrabalhadas = float(input("quantas horas voce trabalhou no mes?"))
salariot = salarioph*horastrabalhadas
impostoderenda = (salariot*11)/100
inss = (salariot*8)/100
sindicato = (salariot*5)/100
valorliquido = salariot-impostoderenda-inss-sindicato
print("salário bruto",salariot," reais." " pago ao imposto de renda",impostoderenda," reais." " pago ao inss",inss," reais." " pago ao sindicato",sindicato," reais." " valor liquido",valorliquido," reais.")
