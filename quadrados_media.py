n1 = 1
f = 7
r = 1
soma = 0
sq = 0
for i in range(n1, f, r):
    soma = soma + i
    quadr = i ** 2
    sq += quadr
    med = (soma + i) / (f - n1)
    print(i,end=' ')
print('\n\nA soma é : ', soma,'\nA soma dos quadrados é: ',sq,'\nA média é: ', med)