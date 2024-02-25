nome = str(input("Digite seu nome completo: ")).split()
print('estou analisando seu nome...')
print("Seu nome em maiusculo é: {}.".format(nome.upper()))
print("Seu nome em minúsculo: {}.".format(nome.lower()))
print("Quantidade de letras ao todo: {}.".format(len(nome)))
# também da pra adc o para tirar contadores de espaço - nome.count(" ")))
separa = nome.split()
print('Seu primeiro nome é "{}" e ele tem {} letras.'.format(separa[0], len(separa[0])))

# confuso