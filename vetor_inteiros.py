vetor = [5, 9, 18, 21, 32, 52]

print(vetor)

vetor2 = []

for valor in vetor:
    if valor % 2 == 0:
        vetor2.append(valor)

print(f"\nNo vetor exposto, existem {vetor2} valores pares.")
