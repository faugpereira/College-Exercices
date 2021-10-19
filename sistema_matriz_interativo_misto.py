import numpy as np

print('Agora você terá a chance de montar sua matriz e descobrir seu determinante, sua inversa e os devidos resultados das incógnitas.'
      '\nPara números inteiros na primeira matriz e flutuantes na segunda com 3 incógnitas')
a11 = int(input('Digite o valor da primeira linha e primeira coluna (a11): '))
a21 = int(input('Digite o valor da segunda linha e primeira coluna (a21): '))
a31 = int(input('Digite o valor da terceira linha e primeira coluna (a31): '))

a12 = int(input('Digite o valor da primeira linha e segunda coluna (a12): '))
a22 = int(input('Digite o valor da segunda linha e segunda coluna (a22): '))
a32 = int(input('Digite o valor da terceira linha e segunda coluna (a32): '))

a13 = int(input('Digite o valor da primeira linha e terceira coluna (a13): '))
a23 = int(input('Digite o valor da segunda linha e terceira coluna (a23): '))
a33 = int(input('Digite o valor da terceira linha e terceira coluna (a33): '))

A = np.array([[a11, a21, a31], [a12, a22, a32], [a13, a23, a33]])
print('\nA = \n',A)

print('Digite os 3 valores da segunda matriz.')
b11 = float(input('Digite o valor da primeira linha e primeira coluna (b11): '))
b21 = float(input('Digite o valor da segunda linha e primeira coluna (b21): '))
b31 = float(input('Digite o valor da terceira linha e primeira coluna (b31): '))

B = np.array([[b11], [b21], [b31]])
print('\nB = \n', B)

detA = np.linalg.det(A)
print('\nDeterminante de A = \n', detA)

inversaA = np.linalg.inv(A)
print('\nA inversa de A = \n', inversaA)

x = inversaA @ B
print('\nX = \n', x)