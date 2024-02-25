from math import hypot
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
hip = hypot(co, ca)
print("A hipotenusa dos números {} e {} é {:.2f}.".format(co, ca, hip))