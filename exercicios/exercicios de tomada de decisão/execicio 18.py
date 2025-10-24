la = float(input("quantos litros de álcool voce comprou?"))
lg = float(input("quantos litros de gasolina voce comprou?"))
ppla = 4.17
pplg = 6.29
pta = la * ppla
ptg = lg*pplg
if la<0 or lg<0:
    print("digite valores válidos")
    exit(1)
if la <= 20:
    pcda = pta * 0.97
    print("voce terá que pagar:",pcda,"reais de álcool")
elif la > 20:
    pcda = pta * 0.95
    print("voce terá que pagar:", pcda, "reais de álcool")
if lg <= 20:
    pcdg = ptg * 0.96
    print("voce terá que pagar:", pcdg, "reais de gasolina")
elif lg > 20:
    pcdg = ptg * 0.94
    print("voce terá que pagar:", pcdg, "reais de gasolina")
precototal = pcdg+pcda
print(" voce terá que pagar",precototal,"reais no total")



