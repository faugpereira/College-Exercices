inteiros = 1
soma_inteiros = 0
qtd_inteiros = 0

while 0 < inteiros != 0:
    inteiros = int(input('Digite um número inteiro: '))
    soma_inteiros = soma_inteiros + inteiros
    qtd_inteiros = qtd_inteiros + 1
media = soma_inteiros / (qtd_inteiros-1)
print('A média de {} números é {}'.format((qtd_inteiros-1), media))