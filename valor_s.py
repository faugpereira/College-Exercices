numerador = 1
denominador = 1
ns = 0

while numerador <= 99 and denominador <= 50:
    s = (numerador/denominador)
    numerador = numerador + 2
    denominador = denominador + 1
    ns = ns + s
print(ns)