from imposto import imposto
for i in range(0, 10):
    print(i)


saldoConta = 5800

if (saldoConta > 3000):
    taxes = imposto(saldoConta, 15)
    print("O valor do seu imposto corresponde a: {}".format(taxes))