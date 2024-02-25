sal = float(input('Qual é o salário do Funcionário R$'))
novosal = sal + (sal * 15 / 100)
print('O funcionário que ganhava R${}, com aumento de 15%, passa a receber R${:.2f}'.format(sal, novosal))
