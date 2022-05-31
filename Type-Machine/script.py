from random import choice
from winsound import Beep

teclas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
tecladas = 0

pesquisa = input('Search:\n|> ')
apagar = True
historic_size = 20

historic = []

while 1:
    tecla = choice(teclas)
    tecladas += 1
    
    historic.append(tecla)
    if len(historic) > historic_size + len(pesquisa) and apagar: historic.pop(0)

    if pesquisa in (''.join(historic)):
        Beep(1000,1000)
        print(''.join(historic), '<<')
        print('\n' + str(tecladas))
        break

input()
