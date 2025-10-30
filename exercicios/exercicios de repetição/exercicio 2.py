idade  = int(input("quantos anos voce tem?"))
while idade <0 or idade >150:
    print("valor invalido, coloque um valor entre 0 e 150")
    idade = int(input("quantos anos voce tem?"))
salario = float(input("qual o seu salario?"))
while salario <=0:
    print("valor invalido, coloque um valor maior que zero")
    salario = float(input("qual o seu salario?"))
estadoc = input("qual o seu estado civil? S-solteiro(a); C-casado(a); V-viuvo(a); D-divorciado(a)")
while estadoc != "C" and estadoc != "S"and estadoc != "V" and estadoc != "D":
    print("valor invalido")
    estadoc = input("qual o seu estado civil? S-solteiro(a); C-casado(a); V-viuvo(a); D-divorciado(a)")
nome = input("qual o seu nome")
while len(nome) <= 3:
    print("valor invalido")
    nome = input("qual o seu nome?")