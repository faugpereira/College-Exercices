h = 0
numerador = 0
denominador = 0
soma = 0
sub = 0
for i in range(1, 11, 1):
    h = i/(i**2)
    sub = -h
    print('{}/{}'.format(i,i**2))
    soma += h
    re =
print('\nA soma dos números acima é: ',soma)