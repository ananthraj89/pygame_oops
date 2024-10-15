import pygame
from pygame.locals import *
import sys
from pydemo6_BallBounceOops import Ball

#2- Define Constants
BLACK = (0,0,0)
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640
FRAMES_PER_SECOND = 30

#3.Initialization of the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4.Load images, sounds, etc.

N_Balls = 10

#5.Initialization of variables
ballList = []
for oBall in range(0, N_Balls):
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)

#6.Loop forever
while True:

    #7.Check for the handle evenets
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #8.Do any perframe actions
    for oBall in ballList:
        oBall.update() #tell Ball to update itself

    #9.Clear the window before drawing it again.
    window.fill(BLACK)

    #10.Draw the window elements
    for oBall in ballList:
        oBall.draw()

    #11.update the window
    pygame.display.update()

    #12.Slow thingsdown a bit
    clock.tick(FRAMES_PER_SECOND)





