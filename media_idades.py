idade = 1
qtd_idade = 0
idade_soma = 0

while idade != 0:
    idade = int(input('Digite uma idade: '))
    qtd_idade = qtd_idade + 1
    idade_soma = idade_soma + idade
print('a idade média de {} pessoas é {}'.format((qtd_idade-1), idade_soma/(qtd_idade-1)))
