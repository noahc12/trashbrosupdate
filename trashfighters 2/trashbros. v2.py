import pygame
from sprites import *
pygame.init()

w = 800
h = 400
screen = pygame.display.set_mode((w, h))

pygame.display.set_caption("Trash.Bros!")

speed = [2, 2]
black = (0, 0, 0)
blue = (0, 0, 255)
p1 = pygame.image.load("Sanrec1.png")
p1_rect = p1.get_rect()


run = True
sprite1 = Player()
sprite2 = Platform(0, 400, 800, 100)
spriteGroup = pygame.sprite.Group()
platform = pygame.sprite.Group()
spriteGroup.add(sprite1)
platform.add(sprite2)
while run:
    pygame.time.delay(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # movement
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and p1_rect > 0:
        p1_rect = p1_rect.move([0, -7])
    if key[pygame.K_DOWN]:
        p1_rect = p1_rect.move([0, 7])
    if key[pygame.K_LEFT]:
        p1_rect = p1_rect.move([-4, 0])
    if key[pygame.K_RIGHT]:
        p1_rect = p1_rect.move([4, 0])

    spriteGroup.update()
    platform.update()
    screen.fill(black)
    spriteGroup.draw(screen)
    platform.draw(screen)
    screen.blit(p1, p1_rect)
    pygame.display.update()