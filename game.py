import pgzrun
import math
import random
from pygame import Rect

# Configurações da Janela
WIDTH = 800
HEIGHT = 600
TITLE = "Shadow Jumper - Platformer"

# Estados do Jogo
MENU = 0
GAME = 1
state = MENU

# Configurações de Áudio
audio_on = True

class AnimatedSprite:
    """Classe base para lidar com movimento e animação cíclica de sprites."""
    def __init__(self, images, x, y):
        self.images = images  # Lista de nomes de imagens para animação
        self.frame = 0
        self.image = images[0]
        self.pos = [x, y]
        self.anim_speed = 0.15
        self.timer = 0

    def update_animation(self):
        self.timer += self.anim_speed
        if self.timer >= len(self.images):
            self.timer = 0
        self.frame = int(self.timer)
        self.image = self.images[self.frame]

class Hero(AnimatedSprite):
    def __init__(self, x, y):
        # Listas com apenas 2 frames cada
        self.idle_r = ["hero_idle_r1", "hero_idle_r2"]
        self.idle_l = ["hero_idle_l1", "hero_idle_l2"]
        self.walk_r = ["hero_walk_r1", "hero_walk_r2"]
        self.walk_l = ["hero_walk_l1", "hero_walk_l2"]
        
        super().__init__(self.idle_r, x, y)
        
        self.vel_y = 0
        self.speed = 4
        self.is_jumping = False
        self.facing_right = True

    def update(self, platforms):
        dx = 0
        
        # Lógica de movimentação
        if keyboard.left:
            dx = -self.speed
            self.images = self.walk_l
            self.facing_right = False
        elif keyboard.right:
            dx = self.speed
            self.images = self.walk_r
            self.facing_right = True
        else:
            # Seleciona o frame de "parado" correto
            if self.facing_right:
                self.images = self.idle_r
            else:
                self.images = self.idle_l

        # Gravidade
        self.vel_y += 0.5
        self.pos[1] += self.vel_y
        
        # Colisão (usando sua medida de 90px de altura)
        hero_rect = Rect(self.pos[0], self.pos[1], 20, 90)
        for plat in platforms:
            if hero_rect.colliderect(plat) and self.vel_y > 0:
                self.pos[1] = plat.top - 90
                self.vel_y = 0
                self.is_jumping = False

        self.pos[0] += dx
        
        # Este método vai ciclar entre frame 0 e 1 automaticamente
        self.update_animation()

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -15
            self.is_jumping = True
            if audio_on:
                sounds.jump.play()

class Enemy(AnimatedSprite):
    def __init__(self, x, y, distance):
        # Definimos as listas de frames para cada direção
        self.walk_right = ["enemy_walk_right1", "enemy_walk_right2"]
        self.walk_left = ["enemy_walk_left1", "enemy_walk_left2"]
        
        # Começamos com a direita
        super().__init__(self.walk_right, x, y)
        
        self.start_x = x
        self.distance = distance
        self.direction = 1 # 1 para direita, -1 para esquerda
        self.speed = 2

    def update(self):
        # Movimentação
        self.pos[0] += self.direction * self.speed
        
        # Lógica de inversão de direção
        if abs(self.pos[0] - self.start_x) > self.distance:
            self.direction *= -1
            
            # TROCA DE IMAGENS:
            if self.direction == 1:
                self.images = self.walk_right
            else:
                self.images = self.walk_left
            
            # Reiniciamos o timer para a animação começar do frame 0 na nova direção
            self.timer = 0 
            
        self.update_animation()

# Inicialização de Objetos
hero = Hero(100, 400)
enemies = [Enemy(300, 350, 100), Enemy(550, 150, 80)]
platforms = [
    Rect(0, 550, 800, 50),   # Chão
    Rect(250, 400, 150, 20), # Plataforma 1
    Rect(500, 200, 150, 20)  # Plataforma 2
]

# Botões do Menu
btn_start = Rect(300, 200, 200, 50)
btn_audio = Rect(300, 300, 200, 50)
btn_exit = Rect(300, 400, 200, 50)

def draw():
    # Limpa a tela antes de desenhar
    screen.clear()
    
    if state == MENU:
        # Desenha o fundo no menu
        screen.blit("background", (0, 0))
        
        # Botões do Menu
        screen.draw.filled_rect(btn_start, "blue")
        screen.draw.text("START GAME", center=btn_start.center, color="white", fontsize=30)
        
        audio_text = "AUDIO: ON" if audio_on else "AUDIO: OFF"
        screen.draw.filled_rect(btn_audio, "green")
        screen.draw.text(audio_text, center=btn_audio.center, color="white", fontsize=30)
        
        screen.draw.filled_rect(btn_exit, "red")
        screen.draw.text("EXIT", center=btn_exit.center, color="white", fontsize=30)
    
    elif state == GAME:
        # 1. Desenha o fundo do cenário
        screen.blit("background", (0, 0))
        
        # 2. Desenha as plataformas (chão e suspensas)
        for plat in platforms:
            screen.draw.filled_rect(plat, "grey")
        
        # 3. Desenha os inimigos
        for en in enemies:
            screen.blit(en.image, (en.pos[0], en.pos[1]))
            
        # 4. Desenha o herói por cima de tudo
        screen.blit(hero.image, (hero.pos[0], hero.pos[1]))
        
def update():
    global state
    if state == GAME:
        hero.update(platforms)
        for en in enemies:
            en.update()
            
            # Ajuste da colisão para bater no inimigo
            hero_rect = Rect(hero.pos[0], hero.pos[1], 40, 50)
            en_rect = Rect(en.pos[0], en.pos[1], 40, 40)
            
            if hero_rect.colliderect(en_rect):
                # TOCAR SOM DE DANO AQUI
                if audio_on:
                    sounds.hit.play() # Certifique-se de ter 'hit.wav' na pasta sounds
                
                hero.pos = [100, 400] # Reset ao morrer
                hero.vel_y = 0        # Zera a velocidade para não nascer caindo

def on_mouse_down(pos):
    global state, audio_on
    if state == MENU:
        if btn_start.collidepoint(pos):
            state = GAME
            if audio_on:
                sounds.background_theme.play(loops=-1)
        elif btn_audio.collidepoint(pos):
            audio_on = not audio_on
            if not audio_on:
                sounds.background_theme.stop()
        elif btn_exit.collidepoint(pos):
            exit()

def on_key_down(key):
    if state == GAME:
        if key == keys.SPACE or key == keys.UP:
            hero.jump()

pgzrun.go()