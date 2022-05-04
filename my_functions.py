import numpy as np

def calcula_media(v):    # para criar uma função tem que usar "def" = define
    
    '''
    Essa função calcula a media dos elementos um array.
    
    Inputs: 
    v: numpy array
    
    Outputs:
    media: escalar
    '''
    
    soma = 0
    for i in v:
        soma += i
    media = soma/len(v)
    
    return media

def calcula_tempo(velocidade, distancia):
    
    '''
    Calcula o tempo a partir da velocidade e distância.
    
    Inputs:
    velocidade: Escalar (m/s)
    distancia: Escalar (m)
    
    Output:
    tempo: Escalar (s)
    '''
    
    tempo = distancia/velocidade

    return tempo

def calcula_distancia(velocidade, tempo):
    
    '''
    Calcula a distância a partir da velocidade e tempo.
    
    Inputs:
    velocidade: Escalar (m/s)
    tempo: Escalar (s)
    
    Output:
    distancia: Escalar (m)
    '''
    
    distancia = velocidade * tempo
    
    return distancia