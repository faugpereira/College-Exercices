import numpy

print("\n1 – Área do quadrado\n2 – Área do triângulo\n3 – Área do círculo\n4 – Área do retângulo\n5 – Encerrar o programa")

f = int(input("\nDigite um número para executar a função desejada: "))

if f == 1:
    l = int(input("\nDigite o lado do quadrado: "))
    a = l**2
    print(a)
elif f == 2:
    b = int(input("\nDigite a base do triângulo: "))
    h = int(input("\nDigite a altura do triângulo: "))
    a = (b*h)/2
    print(a)
elif f == 3:
    r = int(input("\nDigite o raio do circulo: "))
    a = numpy.pi * r**2
    print(a)
elif f == 4:
    b = int(input("\nDigite a base do retângulo: "))
    h = int(input("\nDigite a altura do retângulo: "))
    a = b*h
    print(a)
elif f == 5:
    print("\nO programa foi finalizado!")