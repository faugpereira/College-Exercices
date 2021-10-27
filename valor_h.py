h = 0
for i in range(1,11):
    if (i % 2 == 0):
        i = -(i / i ** 2)
        h = h + i
    else:
        i = i / i ** 2
        h = h + i
    print('{}/{}'.format(i, i ** 2))
print('\nA soma dos números acima é: ',h)