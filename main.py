import pygame
from spritesheet import Spritesheet

WHITE = (255,255,255)
pygame.init()
W,H = 420,270
background = pygame.Surface((W,H))
window = pygame.display.set_mode(((W,H)))
carry_on = True

my_spritesheet = Spritesheet('stay.png')
hero = [my_spritesheet.parse_sprite('walk1.png'),my_spritesheet.parse_sprite('walk2.png'),
        my_spritesheet.parse_sprite('walk3.png')]
index = 0

while carry_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carry_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                index = (index + 1)% len(hero)

    background.fill(WHITE)
    background.blit(hero[index], (0, H - 109))
    window.blit(background,(0,0))
    pygame.display.update()




