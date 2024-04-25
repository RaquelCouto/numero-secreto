for i in range(0, 10):
    print(i)

imposto = 0
saldoConta = 2500

if (saldoConta > 3000):
    imposto = (saldoConta*(15/100))
elif(saldoConta < 3000):
    print("Seu saldo é inelegível para pagar imposto")

print("O valor do seu imposto corresponde a: {}".format(imposto))