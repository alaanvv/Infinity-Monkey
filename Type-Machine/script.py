from random import choice
from winsound import Beep

teclas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
tecladas = 0

pesquisa = input('|> ')
apagar = True
historico_size = 20

historico = []

while 1:
    tecla = choice(teclas)
    tecladas += 1
    
    historico.append(tecla)
    if len(historico) > historico_size + len(pesquisa) and apagar: historico.pop(0)

    if pesquisa in (''.join(historico)):
        Beep(1000,1000)
        print(''.join(historico), '<<')
        print('\n' + str(tecladas))
        break

input()