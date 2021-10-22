n1 = 0
n2 = 1
n = int(input('Digite quantos termos quer conhecer da sequência Fibonacci: '))
for f in range(0, n):
    p = n1 + n2
    n1 = n2
    n2 = p
    print(p)