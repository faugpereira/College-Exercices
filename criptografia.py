import numpy as np

mensagem = input('Escreva a frase que deseja criptografar: ')
chave = input('Escreva uma palavra chave para criptografar a frase: ')

for caracter in mensagem:
     ind = chr(caracter)
     if chr(32) <= or >= chr(127):
         np.array([[ind, ind, 2], [6, 4, 5], [2, 2, 1]])
print('\nA = \n',A)


B = np.array([[42.50], [68.50], [23.50]])
print('\nB = \n', B)


detA = np.linalg.det(A)
print('\nDeterminante de A = \n', detA)


inversaA = np.linalg.inv(A)
print('\nA inversa de A = \n', inversaA)


x = inversaA @ B
print('\nX = \n', x)



for caracter in mensagem:
    ind = ord(caracter)
    if ord('A') <= ind <= ord('Z')or ord('a') <= ind <=ord('z'):
        nova_letra = chr((ind + chave)%n)

        # substituir na mensagem a letra pela nova_letra
        cifrada = cifrada + nova_letra

        nA = ord('A')
        nZ = ord('Z')
        na = ord('a')
        nZ = ord('z')

        if (ind + chave) <= nZ:
            nova_letra = chr(ind + chave)
        else:
            nova_letra = (ind + chave) % (nZ + 1) + nA

            nova_letra = chr((ind + chave) % (nZ + 1) + ((ind + chave) // (nZ + 1)) * nA)

for caracter in mensagem:
    ind = ord(caracter)
    if nA <= ind <= nZ:
        nova_letra = chr((ind + chave) % (nZ + 1) + ((ind + chave) // (nZ + 1)) * nA)
        # substituir na mensagem a letra pela nova_letra
        cifrada = cifrada + nova_letra
    elif na <= ind <= nz:
        nova_letra = chr((ind + chave) % (nz + 1) + ((ind + chave) // (nz + 1)) * na)
        cifrada = cifrada + nova_letra

    elif ind in range(na, nz + 1):
        nova_letra = chr((ind + chave) % (nz + 1) + ((ind + chave) // (nz + 1)) * nA)
        cifrada = cifrada + nova_letra

    chave = 3
    mensagem = "Em noite de lua cheia, enquanto o Canguçu esturra, o Guatipuru sobe na Carapanaúba?"
    nA = ord('A')
    nZ = ord('Z')
    na = ord('a')
    nz = ord('z')
    for caracter in mensagem:
        ind = ord(caracter)
        if nA <= ind <= nZ:
            nova_letra = chr((ind + chave) % (nZ + 1) + ((ind + chave) // (nZ + 1)) * nA)
            # substituir na mensagem a letra pela nova_letra
            cifrada = cifrada + nova_letra
        elif ind in range(na, nz + 1):
            nova_letra = chr((ind + chave) % (nZ + 1) + ((ind + chave) // (nZ + 1)) * nA)
            cifrada = cifrada + nova_letra
        else:
            cifrada = cifrada + caracter
    print("Original: ", mensagem)
    print("Cifrada: ", cifrada)