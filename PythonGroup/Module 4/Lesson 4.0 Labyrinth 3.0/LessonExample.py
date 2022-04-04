from pygame import * 
import pygame 
from os import path

img_dir = path.join(path.dirname(__file__), 'img') 
WIDTH = 361
HEIGHT = 510
FPS = 30  

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# Создаем игру и окно
pygame.init() 
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinth / Demo ")
clock = pygame.time.Clock()




class Player(pygame.sprite.Sprite):
    speedx = 0
    speedy = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
    def update(self):
        # обработка нажатия клавиш
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8

        self.rect.x += self.speedx
        self.rect.y += self.speedy 

        

        # реализовать тоже самое для высоты :) 
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0 

class Wall(pygame.sprite.Sprite):

    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(wall_img, (100, 10))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = posY
        self.rect.bottom = posX
        



def DrawWin():   
    screen = pygame.display.set_mode((800  , HEIGHT))
    pygame.display.set_caption("Win / Demo ")
    background = pygame.image.load(path.join(img_dir, "win.jpg")).convert()
    background_rect = background.get_rect()
    screen.blit(background, background_rect) 
    pygame.display.flip() 

def DrawGame(): 
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen) 
    pygame.display.flip()


background = pygame.image.load(path.join(img_dir, "labyrinth_field.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "player.png")).convert() 
wall_img = pygame.image.load(path.join(img_dir, "wall.png")).convert()


all_sprites = pygame.sprite.Group() 
player = Player()
wall1 = Wall(300, 180)
wall2 = Wall(200, 90)
wall3 = Wall(400, 300)
wall4 = Wall(400, 90)
wall5 = Wall(200, 300)


walls = list()
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)
walls.append(wall4)
walls.append(wall5)

all_sprites.add(player) 
all_sprites.add(wall1)
all_sprites.add(wall2)
all_sprites.add(wall3)
all_sprites.add(wall4)
all_sprites.add(wall5)

# Цикл игры
running = True
win = False
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for eachWall in walls:
        if(sprite.collide_rect(player, eachWall)):
            running = False

    

    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()   
    if win:
        DrawWin()
    else:
        DrawGame() 
        
    if player.rect.y < 166:
        win = True 

    print(player.rect.x, player.rect.y)




  