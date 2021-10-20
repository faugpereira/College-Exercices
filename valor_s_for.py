numerador = 1
denominador = 1
ns = 0

for numerador in range(1, 100, 2):
    print('{}/{}'.format(numerador,denominador))
    s = (numerador/denominador)
    denominador = denominador + 1
    ns = ns + s
print(ns)