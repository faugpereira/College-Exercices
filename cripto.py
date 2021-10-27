frase = input('Mensagem: ')
chave = input('Chave: ')
i = 0
while i < len(frase):
    c_frase = ord(frase[i])
    c_chave = ord(chave[i % len(chave)])
    print(chr(c_frase ^ c_chave))
    i += 1