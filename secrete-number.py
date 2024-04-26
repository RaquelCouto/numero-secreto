from imposto import *

#variables
valorCompra = 4000
valorCompraImportada = 20000
saldoConta = 5800
palavra = 'Raquel'
salario = 25000


#calling functions
for i in range(0, 20):
    print("o quadrado de {} é: {}".format(i, i*i))

for letra in palavra:
    print(letra)

if (saldoConta > 3000):
    taxes = imposto(saldoConta, 15)
    print("O valor do seu imposto corresponde a: {}".format(taxes))

print('O valor da sua comprinha da Shein é {}'.format(compraShein(valorCompra)))

print('O valor da sua compra importada com ioF vai ser de: {}'.format(ioF(valorCompraImportada, 4.38)))

print("O valor do imposto de renda para o salário de {} é: ".format(salario, impostoDeRenda(salario,27,5)))