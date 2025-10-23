p1 = float(input("qual o preço do primeiro produto?"))
p2 = float(input("qual o preço do segundo produto?"))
p3 = float(input("qual o preço do terceiro produto?"))
if p1<p2 and p1<p3:
    print("voce deve comprar o primeiro produto")
elif p2<p1 and p2<p3:
    print("voce deve comprar o segundo produto")
elif p3<p1 and p3<p2:
    print("voce deve comprar o terceiro produto")
else:
    print("o preço dos produtos é o mesmo")