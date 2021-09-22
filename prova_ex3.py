x = int(input('\nDigite o valor de x: '))

if x == 0:
    f = 1

elif x > 0:
    f = x - 1

elif x < 0:
    f = x + 1

print('\nSe x for igual a', x, ' temos como resultado: ', f)