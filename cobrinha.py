#config inicial.
import pygame as py
import random

py.init()
py.display.set_caption("jogo snake python")
largura, altura = 1200, 800
tela = py.display.set_mode((largura,altura))
relogio = py.time.Clock() #controlador de tempo para limitar frames

#core

preto = (0,0,0)
branca= (255,255,255)
vermelho= (255,0,0)
verde= (0,255,0)

#parametro cobra
tamanho_quadrado = 20
velocidade_jogo = 15

def comida():
    comida_x =round(random.randrange(0,largura - tamanho_quadrado)/20.0)*20.0 
    comida_y =round(random.randrange(0,altura - tamanho_quadrado)/20.0)*20.0 
    return comida_x,comida_y


def desenhar_comida(tamanho,comida_x,comida_y):
    py.draw.rect(tela,verde,[comida_x,comida_y,tamanho,tamanho])

def desenhar_cobra(tamanho,pixels):
    for pixel in pixels:
        py.draw.rect(tela,branca,[pixel[0],pixel[1], tamanho,tamanho])    

def desenhar_pontuacao(pontuacao):
    fonte = py.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontuação:{pontuacao}", True, vermelho)
    tela.blit(texto,[520,7])

def selecionar_velocidade(tecla):
    if tecla == py.K_DOWN:
        velocidade_x= 0
        velocidade_y = tamanho_quadrado
    elif tecla == py.K_UP:
        velocidade_x= 0
        velocidade_y = -tamanho_quadrado
    elif tecla == py.K_RIGHT:
        velocidade_x= tamanho_quadrado
        velocidade_y = 0
    elif tecla == py.K_LEFT:
        velocidade_x= -tamanho_quadrado
        velocidade_y =  0           
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x= largura/2
    y= altura/2
    velocidade_x= 0
    velocidade_y= 0

    tamanho_cobra = 1
    pixels= []

    comida_x,comida_y = comida()
      

    while not fim_jogo:
        tela.fill(preto)

        for evento in py.event.get():
            if evento.type == py.QUIT:
                fim_jogo = True
            elif evento.type==py.KEYDOWN:
                velocidade_x,velocidade_y = selecionar_velocidade(evento.key)

            #att posicao    
                #movimentação da cobra pelo tecl
        # desenha os objetos do jogo na tela
        # comida
        desenhar_comida(tamanho_quadrado, comida_x,comida_y)
        # cobrinha
        if x <0 or x>= largura or y <0 or y>=altura:
            fim_jogo =True
            

        x += velocidade_x
        y += velocidade_y    
        pixels.append([x,y])
        if len(pixels)> tamanho_cobra:
            del pixels[0]
        
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fim_jogo = True
        desenhar_cobra(tamanho_quadrado, pixels)            
        # pontuaçao
        desenhar_pontuacao(tamanho_cobra- 1)

        #att tela
        py.display.update()
        if x == comida_x and y == comida_y:
            tamanho_cobra+=1
            comida_x,comida_y = comida()

        relogio.tick(velocidade_jogo)
rodar_jogo()