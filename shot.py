import pygame
import random

class Shot(pygame.sprite.Sprite):
    def __init__(self, group, window_size):
        super().__init__(group)

        self.WINDOW_SIZE = window_size
        self.image = pygame.image.load("data/images/shot.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [28, 8])
        self.rect = self.image.get_rect()

        self.speed = 7

    def update(self):
        self.rect[0] += self.speed

        if self.rect[0] > self.WINDOW_SIZE[0]:
            self.kill()
