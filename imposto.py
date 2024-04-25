def imposto(salario, taxa):
    imposto = salario*(taxa/100)
    return imposto


def deducaoImposto(salario):
    if (salario < 3000):
        reducaoImposto = salario*(3/100)
        return reducaoImposto