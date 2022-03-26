# Libs

from time import sleep 
from random import randint, choice
import pyttsx3

# Setup

engine = pyttsx3.init()

engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0")
def leitura(guincho):
    engine.say(guincho)
    engine.runAndWait()

file = open('mamaco_config.txt', 'r').read().split('\n')

NOME_DO_MACACO = file[0].split('=')[1]
MINIMO_DE_PALAVRAS = int(file[1].split('=')[1])
MAXIMO_DE_PALAVRAS = int(file[2].split('=')[1])
INTERVALO = int(file[3].split('=')[1])
PESQUISA = file[4].split('=')[1]
TIPO_DE_ESTUDO = file[5].split('=')[1]
LEITURA_MODE = int(file[6].split('=')[1])

DICIONARIO_DO_MAMACO = open('dicionario.txt', 'r').read().split('\n') # Dicionário entregado ao seu macaco, ele não saberá significados nem regras de português

# Uh-uh-ah-ah

def digitar(): # Comando para o macaco escrever UMA frase, ele não se incomoda
    numero_de_palavras = randint(MINIMO_DE_PALAVRAS, MAXIMO_DE_PALAVRAS)
    palavras = []

    for x in range(numero_de_palavras):
        palavras.append(choice(DICIONARIO_DO_MAMACO)) # Macacos não seguem lógicas

    return (' '.join(palavras)).capitalize()

def macacar_sem_fim(): # Essa parte realmente incomoda os macacos, mas eles recebem uma banana durante os intervalos e isso anula tudo
    while 1:
        frase_do_macaco = digitar()
        print(frase_do_macaco)
        if LEITURA_MODE == 1: leitura(frase_do_macaco)
        else: sleep(INTERVALO) # Esse é o tempo que eles levam pra comer uma banana

def pesquisa_primata(frase_pesquisada=''):
    print('Cientista: -Seu macaco acaba de ganhar um teclado!\n')

    frase_pesquisada = frase_pesquisada.lower()
    contador_de_frases = 0

    while 1:
        contador_de_frases += 1
        frase_do_macaco = digitar().lower()

        if frase_do_macaco ==  frase_pesquisada:
            print(NOME_DO_MACACO + ': -MACACO SER ESPERTO OLHA O QUE MACACO ESCREVER')
            print(frase_do_macaco, '\n')
            if LEITURA_MODE == 1: leitura(frase_do_macaco)
            print('Cientista: -Seu macaco escreveu {} frases'.format(contador_de_frases))

            break

# Mesa do macaco

if TIPO_DE_ESTUDO == '1': 
    frase_do_macaco = digitar()
    print(frase_do_macaco)
    if LEITURA_MODE == 1: leitura(frase_do_macaco)
    input('ENTER')

elif TIPO_DE_ESTUDO == '2':
    macacar_sem_fim()

elif TIPO_DE_ESTUDO == '3':
    pesquisa_primata(PESQUISA)
    input('ENTER')

else: 
    print('Erro no tipo de estudo!')
    input('ENTER')