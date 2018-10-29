import sys, pygame


def events():

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()


pygame.init()
width = 800
height = 400
heightwidth, HH = width / 2, height / 2
AREA = width * height
# resize png to 800x600

screen = pygame.display.set_mode((width,height))
speed = [1, 1]
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
background = pygame.image.load("mountains.png").convert()

backgroundwidth, backgroundgheight = background.get_rect().size

stageWidth = backgroundwidth * 2
stagePosX = 0

startScrollingPosX = heightwidth
circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 400
playerVelocityX = 0


class Player1:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sanrec.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = width - 30
        self.rect.bottom = height - 40
        self.speedx = 0

    def update(self):
        self.speedx = 0
        k = pygame.key.get_pressed()

        if k[pygame.K_RIGHT]:
            self.speedx = 6

        if k[pygame.K_LEFT]:
            self.speedx = -6

        self.rect.x += self.speedx






# main loop
# while True:
#     events()
#
#     k = pygame.key.get_pressed()
#
#     if k[pygame.K_RIGHT]:
#         playerVelocityX = 1
#     elif k[pygame.K_LEFT]:
#         playerVelocityX = -1
#     else:
#         playerVelocityX = 0
#
#     playerPosX += playerVelocityX
#     if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
#     if playerPosX < circleRadius: playerPosX = circleRadius
#     if playerPosX < startScrollingPosX:
#         circlePosX = playerPosX
#     elif playerPosX > stageWidth - startScrollingPosX:
#         circlePosX = playerPosX - stageWidth + width
#     else:
#         circlePosX = startScrollingPosX
#         stagePosX += -playerVelocityX
#
#     rel_x = stagePosX % backgroundwidth
#     screen.blit(background, (rel_x - backgroundwidth, 0))
#     if rel_x < width:
#         screen.blit(background, (rel_x, 0))
#
#     pygame.draw.circle(screen, WHITE, (int(circlePosX), playerPosY - circleRadius), circleRadius, 0)

#
#
#  scrolling image
#  p1 = pygame.image.load("player1.png")
#  p1_rect = p1.get_rect()
#  while 1:
#      for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#              sys.exit()
#
#      p1_rect = p1_rect.move(speed)
#      if p1_rect.left < 0 or p1_rect.right > width:
#          speed[0] = -speed[0]
#      if p1_rect.top < 0 or p1_rect.bottom > height:
#          speed[1] = -speed[1]
#
#      key = pygame.key.get_pressed()
#      if key[pygame.K_UP]:
#          p1_rect = p1_rect.move([0, -2])
#     if key[pygame.K_DOWN]:
#          p1_rect = p1_rect.move([0, 2])
#     if key[pygame.K_LEFT]:
#          p1_rect = p1_rect.move([-6, 0])
#      if key[pygame.K_RIGHT]:
#          p1_rect = p1_rect.move([6, 0])
# 
#     screen.fill(black)
#      screen.blit(p1, p1_rect)
#     pygame.display.flip()