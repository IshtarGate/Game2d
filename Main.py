#initializing
import pygame
pygame.init()
size = width, height = 300, 200
screen=pygame.display.set_mode(size)

isRunning=1
playerPos=[int(width/2),int(height/2)]
#keys
pygame.key.set_repeat (20, 20)

#colors
black=(0,0,0)
white=(255,255,255)

clock=pygame.time.Clock()


while isRunning:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning=0 #change isRunning to false
    screen.fill(black)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:#left or -x
        playerPos[0]-=1
    if keys[pygame.K_d]:#right or +x
        playerPos[0]+=1
    if keys[pygame.K_w]:#up or -y
        playerPos[1]-=1
    if keys[pygame.K_s]:#down or +y
        playerPos[1]+=1

    pygame.draw.rect(screen, white, [playerPos[0],playerPos[1], 2, 2], 0)

    """
    LEFT OFF ANALYSIS HERE, TALKING ABOUT HOW WE
    WOULD HAVE MADE OUR OWN RECTANGLES START FROM
    CENTER INSTEAD OF TOP LEFT
    """

    #pygame.draw.circle(screen,white,[playerPos[0], playerPos[1]], 1)
    #key presses
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 isRunning=0
#             if event.key == pygame.K_a:
#                 playerPos[0]-=1
#             if event.key == pygame.K_d:
#                 playerPos[0]+=1
#             if event.key == pygame.K_w:
#                 playerPos[1]-=1
#             if event.key == pygame.K_s:
#                 playerPos[1]+=1

    pygame.display.flip()
    initialized=1

pygame.quit(); #idle friendly