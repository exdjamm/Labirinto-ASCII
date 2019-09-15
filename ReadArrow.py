# -*- coding: utf-8 -*-

# Codigo de leitura das setas
from readchar  import readkey 
from readchar import key
# Inclue os codigos para poder ler (nao  sei como funciona) 


"""
Codigo para ler as setas e retorna qual seta foi precisionada:

1 para o eixo Y
    -1 para ir para cima (subtrai a posiçao antiga do jogador)
    1 para ir para baixo (soma a posiçao antiga do jogador)
2 para o eixo X
    mesma logica, -1 para esquerda, 1 para direita 
"""
def readKey():
    try:
        keypress = readkey() # Le a tecla

        if keypress == key.UP: # Testa se a tecla é a seta para a cima
            return 1, -1
        elif keypress == key.DOWN:# Testa se a tecla é a seta para a baixo
            return 1, 1
        elif keypress == key.LEFT:# Testa se a tecla é a seta para a esquerda
            return 2, -1
        elif keypress == key.RIGHT:# Testa se a tecla é a seta para a direira
            return 2, 1
        else: # Caso nao for nenhuma das teclas das setas, retorna 0, 0
            return 0, 0
    except KeyboardInterrupt:
        pass

