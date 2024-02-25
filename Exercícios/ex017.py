from math import trunc
num = float(input("Digite um número real: "))
print("Valor digitado: {} e a sua porção inteira: {}.".format(num, int(num)))
print("Valor digitado: {} e a sua porção inteira: {}.".format(num, trunc(num)))