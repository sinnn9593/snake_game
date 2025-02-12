import pygame
import random

class Food:
    def __init__(self, block_size):
        self.block_size = block_size
        self.position = [0, 0]

    def respawn(self, width, height):
        self.position = [
            round(random.randrange(0, width - self.block_size) / 10.0) * 10.0,
            round(random.randrange(0, height - self.block_size) / 10.0) * 10.0
        ]

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, [self.position[0], self.position[1], self.block_size, self.block_size])
