real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 4.93
print('Com R${} reais você pode comprar US${:.2f}'.format(real, dolar))