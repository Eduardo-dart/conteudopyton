anos = 0
pa = int(input("quantas pessoas tem a cidade A?"))
pb = int(input("quantas pessoas tem a cidade B?"))
taxaa = float(input("qual a porcentagem do crescimento anual da cidade A?"))
taxab = float(input("qual a porcentagem do crescimento anual da cidade B?"))
taxaa = taxaa/100 +1
taxab = taxab/100 +1
while taxaa<taxab:
    print("a cidade A nunca vai passar a B")
    taxaa = float(input("qual a porcentagem do crescimento anual da cidade A?"))
    taxab = float(input("qual a porcentagem do crescimento anual da cidade B?"))
    taxaa = taxaa / 100 + 1
    taxab = taxab / 100 + 1

while pa < pb:
    pa = pa * taxaa
    pb = pb * taxab
    anos = anos + 1
print(f"fora necessarios {anos} anos para o pais A passar o pais B em população")