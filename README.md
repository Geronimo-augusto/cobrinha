# Jogo da Cobrinha em Python com Pygame

## Descrição
Este é um simples jogo da cobrinha desenvolvido em Python utilizando a biblioteca Pygame.
O objetivo do jogo é controlar a cobra e coletar a comida que aparece aleatoriamente na tela.
Cada vez que a cobra come a comida, ela cresce de tamanho. O jogo termina quando a cobra colide com as bordas da tela ou com ela mesma.

# Instalação
Para executar o jogo, você precisa ter o Python e a biblioteca Pygame instalados. Se ainda não tiver, você pode instalá-los utilizando os seguintes comandos:

```bash
pip install pygame
```

## Como jogar
- Utilize as setas do teclado para mover a cobra:
  - Seta para cima: move a cobra para cima
  - Seta para baixo: move a cobra para baixo
  - Seta para a esquerda: move a cobra para a esquerda
  - Seta para a direita: move a cobra para a direita
- O jogo termina se a cobra colidir com as bordas da tela ou com ela mesma.
- A pontuação é exibida no topo da tela.

## Código
``` python
  import pygame as py
import random

# Inicialização do Pygame
py.init()
py.display.set_caption("Jogo Snake Python")
largura, altura = 1200, 800
tela = py.display.set_mode((largura, altura))
relogio = py.time.Clock()  # Controlador de tempo para limitar frames

# Cores
preto = (0, 0, 0)
branca = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# Parâmetros da cobra
tamanho_quadrado = 20
velocidade_jogo = 15

# Função para gerar a posição da comida aleatoriamente
def comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

# Função para desenhar a comida na tela
def desenhar_comida(tamanho, comida_x, comida_y):
    py.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

# Função para desenhar a cobra na tela
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        py.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

# Função para desenhar a pontuação na tela
def desenhar_pontuacao(pontuacao):
    fonte = py.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontuação: {pontuacao}", True, vermelho)
    tela.blit(texto, [520, 7])

# Função para selecionar a direção da cobra baseada na tecla pressionada
def selecionar_velocidade(tecla):
    if tecla == py.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == py.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == py.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == py.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

# Função principal para rodar o jogo
def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = comida()

    while not fim_jogo:
        tela.fill(preto)

        for evento in py.event.get():
            if evento.type == py.QUIT:
                fim_jogo = True
            elif evento.type == py.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        # Atualiza a posição da cobra
        x += velocidade_x
        y += velocidade_y    
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # Verifica colisão com as bordas
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # Verifica colisão com o próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        # Desenha os objetos do jogo na tela
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)

        # Atualiza a tela
        py.display.update()

        # Verifica se a cobra comeu a comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = comida()

        relogio.tick(velocidade_jogo)

# Inicia o jogo
rodar_jogo()
```
## Observações
- Certifique-se de ter o Pygame instalado antes de executar o código.
- O jogo pode ser encerrado fechando a janela do Pygame.
- A velocidade da cobra pode ser ajustada alterando o valor da variável velocidade_jogo.
Divirta-se jogando!
