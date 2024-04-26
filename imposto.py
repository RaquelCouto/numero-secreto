def imposto(salario, taxa):
    imposto = salario*(taxa/100)
    return imposto


def deducaoImposto(salario):
    if (salario < 3000):
        reducaoImposto = salario*(3/100)
        return reducaoImposto
    
def quadradoNumero(numero):
    return numero*numero

def impostoShein(valorCompra):
    imposto = 0
    if (valorCompra > 200):
        imposto = valorCompra*(10/100)
    else:
        imposto = 0
    return imposto

def compraShein(valorCompra):
    totalCompra = impostoShein(valorCompra) + valorCompra
    return totalCompra