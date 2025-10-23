salario = float(input("qual o seu salario atual?"))
if salario <= 1450.99:
    salarionovo =salario*1.20
    salarioaumentado = salarionovo-salario
    print("Antes voce ganhava",salario,"agora você teve um aumento de 20%(",salarioaumentado,") reais, seu novo salario é",salarionovo,"reais")

elif salario >=1451 and salario < 2800:
    salarionovo =salario*1.15
    salarioaumentado = salarionovo-salario
    print("Antes voce ganhava",salario,"agora você teve um aumento de 15%(",salarioaumentado,") reais, seu novo salario é",salarionovo,"reais")

elif salario >=2800 and salario<3500:
    salarionovo =salario*1.1
    salarioaumentado = salarionovo-salario
    print("Antes voce ganhava",salario,"agora você teve um aumento de 10%(",salarioaumentado,") reais, seu novo salario é",salarionovo,"reais")

elif salario > 3500:
    salarionovo =salario*1.05
    salarioaumentado = salarionovo-salario
    print("Antes voce ganhava",salario,"agora você teve um aumento de 5%(",salarioaumentado,") reais, seu novo salario é",salarionovo,"reais")