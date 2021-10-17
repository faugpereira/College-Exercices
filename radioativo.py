massa_inicial = float(input('Digite a massa inicial do material em gramas: '))
massa = massa_inicial
segundo = 0
while massa > 0.5:
    massa = (massa/2)
    segundo = segundo + 50
    minuto = segundo/60
    hora = minuto/60
print('Para uma massa inicial de {} gramas e massa final {} gramas\n'
      'Serão {:.0f} horas {:.0f} minutos e {} segundos.'.format(massa_inicial, massa, hora, minuto, segundo%60))