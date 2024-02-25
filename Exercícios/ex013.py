preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O preço já com o desconto é de R${:.2f}'.format(novo))