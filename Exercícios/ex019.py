from math import sin, cos, tan, radians
ang = float(input("Digite um ângulo de uma circunferência: "))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print("O angulo de {} tem o seno de {:.2f}.".format(ang, s))
print("O angulo de {} tem o cosseno de {:.2f}.".format(ang, c))
print("O angulo de {} tem a tangente de {:.2f}.".format(ang, t))