n1 = 0
n2 = 1
n = int(input('Digite quantos termos quer conhecer da sequência Fibonacci: '))
print(n1,'- ',n2,'- ', end='')
for f in range(0, n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3,'- ', end='')