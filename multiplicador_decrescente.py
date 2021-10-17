n = int(input('Digite um número inteiro positivo: '))
ns = n * (n-1)
n = n-2
while n >= 1:
    ns = ns * n
    n = n - 1
print(ns)