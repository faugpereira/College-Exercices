denominador = int(input('Digite um número inteiro positivo: '))
nc = 1
nd = denominador
s = 0
while nd > 0:
    s = s + (nc/nd)
    nc = nc + 1
    nd = nd - 1
print(s)