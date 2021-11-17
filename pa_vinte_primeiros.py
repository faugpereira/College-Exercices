a1 = 5                  # número inicial da PA
r = 6                   # razão da PA
n = 20                  # termos da PA
a2 = a1 + (n) * r       # útltimo termo da PA  > a fórmula é an = a1 + (n - 1) * R
sn = (a1 + a2) * n /2   # soma dos termos da PA
soma = 0
for i in range(a1, a2, r):
    print(i,'- ',end='')
    soma += + i
print('\n\nA somatória dos termos da P.A. é: ',soma)