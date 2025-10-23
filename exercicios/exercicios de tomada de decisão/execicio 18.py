la = float(input("quantos litros de alcool voce comprou?"))
lg = float(input("quantos litros de gasolina voce comprou?"))
ppla = 4.17
pplg = 6.29
pta = la * ppla
if la <= 20:
    pcda = pta * 0.97
elif la > 20:
    pcda = pta * 0.095

