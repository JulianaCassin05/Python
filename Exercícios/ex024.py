num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Número fatiado em Unidade: {}".format(u))
print("Número fatiado em Dezena: {}".format(d))
print("Número fatiado em Centena: {}".format(c))
print("Número fatiado em Milhar: {}".format(m))