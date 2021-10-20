numerador = 1
denominador = 1
ns = 0

for numerador in range(1, 100, 2):
    print('{}/{}'.format(numerador,denominador))
    numerador = numerador + 2
    denominador = denominador + 1
    s = (numerador/denominador)
    ns = ns + s
print(ns)