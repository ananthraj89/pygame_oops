import pygame
from pygame.locals import *
import random

class Ball():
    def __init__(self, window, windowwidth, windowHeight):
        self.window = window
        self.windowwidth = windowwidth
        self.windowHeight = windowHeight

        # Load and scale the ball image
        self.image = pygame.image.load('C:\\Users\\18073\\Desktop\\Data Analyst\\Pygame_practice\\Oops_pygame\\ball.png')
        image_width_height = 100  # Set a size for the scaled image
        self.new_ball_Image = pygame.transform.scale(self.image, (image_width_height, image_width_height))

        # Use the scaled image dimensions for bounds
        self.width = self.new_ball_Image.get_width()
        self.height = self.new_ball_Image.get_height()

        # Adjust maxwidth and maxHeight to prevent the ball from going outside the window
        self.maxwidth = max(0, windowwidth - self.width)
        self.maxHeight = max(0, windowHeight - self.height)

        # Pick a random starting position within the bounds
        self.x = random.randrange(0, self.maxwidth + 1)
        self.y = random.randrange(0, self.maxHeight + 1)

        # Choose random speed between -4 to 4 (Not 0) in both x and y directions
        speedLists = [-10, -3, -2, -1, 1, 2, 3, 10]
        self.xSpeed = random.choice(speedLists)
        self.ySpeed = random.choice(speedLists)

    def update(self):
        # Check if the ball is hitting the wall; if so, change direction
        if (self.x < 0) or (self.x >= self.maxwidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Update the ball's position using the speed in both directions
        self.x += self.xSpeed
        self.y += self.ySpeed

    def draw(self):
        # Draw the scaled ball image at its current position
        self.window.blit(self.new_ball_Image, (self.x, self.y))
