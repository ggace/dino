import pygame
import Util.util as util
import random

def showimg(img, x,y):
    screen.blit(img, (x,y))

t = pygame.init()
pygame.display.set_caption("파이 게임") #<title>

width = 800
height = 600

#dino
dinoWidth = 50
dinoHeight = 50
dinoX = width/9
dinoY = height/2 - dinoHeight/2
dino = util.getimg(r"resources/image/dino.png")
dino = pygame.transform.scale(dino, (dinoWidth, dinoHeight))

#obstacle
obstacleWidth = 30
obstacleHeight = 50
obstacleX = width
obstacleY = height/2 - dinoHeight/2
obstacle = util.getimg(r"resources/image/obstacle.png")
obstacle = pygame.transform.scale(obstacle, (obstacleWidth, obstacleHeight))

screen  = pygame.display.set_mode((width, height))

finish = False

isSpacePress = False
isDinoUp = True
isStart = False

while not(finish):
    pressed = pygame.key.get_pressed()

    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if pressed[pygame.K_SPACE]:
            if(isStart):
                isSpacePress = True
            else:
                isStart = True
                if(dinoY < height/2 - 100):
                    isDinoUp = False
                elif(dinoY == height/2 - dinoHeight/2):
                    isDinoUp = True
                    isSpacePress = False
                if(isDinoUp):
                    dinoY -= 0.8
                else:
                    dinoY += 0.8
                print("start")
    
    
    if(isStart):
        if isSpacePress:
            if(dinoY < height/2 - 150):
                isDinoUp = False
            elif(dinoY >= height/2 - dinoHeight/2):
                isDinoUp = True
                isSpacePress = False
            if(isDinoUp):
                dinoY -= 0.8
            else:
                dinoY += 0.8 
        if obstacleX-obstacleWidth > 0:
            obstacleX -= 0.7
        else:
            obstacleX = width + random.randint(0, 200)
        print(obstacleX)

    
    showimg(dino, dinoX, dinoY)
    showimg(obstacle, obstacleX, obstacleY)
    pygame.draw.line(screen, (0,0,0), [0, height/2+50-20], [width, height/2+50-20])

    pygame.display.flip()