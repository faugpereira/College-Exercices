a1 = 0
r = int(input('Digite a razão R da P.A.: '))
n = int(input('Digite quantos termos terá a PA: '))
a2 = a1 + (n) * r     # a fórmula é an = a1 + (n - 1) * R
sn = (a1 + a2) * n /2 # soma dos termos da PA
soma = 0
for i in range (a1, a2, r):
    print(i)
    soma += + i
print('\nA somatória dos termos da P.A. é: ',soma)