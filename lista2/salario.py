Funcionario = input()
Salario = float(input ())
NS = float(Salario) + float(Salario*0.25)
print ("Prezado %s, a partir hoje você receverá R$%.2f" % (Funcionario, NS))
#Aparentemente, o mix de tipos de entradas de dados é uma das possibilidades para funcionar, porem nao acho que seja o correto.