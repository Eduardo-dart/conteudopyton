nota1 = float(input("qual a sua primeira nota?"))
nota2 = float(input("qual a sua segunda nota?"))
media = (nota1 + nota2)/2
if media >= 7:
    print("APROVADO")
elif media == 10:
    print("ALUNO DESTAQUE")
elif media < 0 or media > 10:
    print("coloque valores entre 0 e 10")
else:
    print("REPROVADO")