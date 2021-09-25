a = float(input('Digite sua altura (em m): '))
p = float(input('Digite seu peso (em kg): '))

imc = p/(a**2)

print('Seu IMC é {:.3f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso')

elif 18.5 <= imc and imc <= 25.0:
    print('Você está com o peso normal')

elif 25.0 < imc and imc <= 30.0:
    print('Você está acima do peso')

elif imc > 30:
    print('Você está obeso')
