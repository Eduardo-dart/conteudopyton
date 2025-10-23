sph = float(input("quantos reais voce ganha por hora trabalhada?"))
ht = int(input("quantas horas voce trabalhou?"))
sb = ht*sph
sindicato = 0.03
fgts = sb*0.11
if sb <=900:
    ps = b=sb*sindicato
    ir = 0
    pir = sb * (ir)/100
    sl = sb * 0.97
elif sb <= 1500:
    ps = b = sb * sindicato
    ir = 5
    pir = (sb * ir) / 100
    sl = sb * 0.92
elif sb <= 2500:
    ps = b = sb * sindicato
    ir = 10
    pir = (sb * ir) / 100
    sl = sb * 0.87
elif sb > 2500:
    ps = b = sb * sindicato
    ir = 20
    pir = (sb * ir) / 100
    sl = sb * 0.77

print("salario bruto :",sph,"*",ht,"     R$:",sb)
print("- Importo de renda(",ir,"%)       R$:",pir)
print("- sindicato(3%)                   R$:",ps)
print(" FGTS:                            R$:",fgts)
print(" total de descontos               R$:",sb - sl)
print("salario liquido                   R$:",sl)