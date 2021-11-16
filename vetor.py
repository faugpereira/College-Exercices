vetor = [5, 9, 18, 21, 32, 52]

print(vetor)

idx = len(vetor) - 1
newList = []

while (idx >= 0):
    newList.append(vetor[idx])
    idx = idx - 1
print("\nA inversão do vetor é: ", newList)