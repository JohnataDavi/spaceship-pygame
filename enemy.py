import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load("data/images/enemy-0.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [70, 90])
        self.rect = self.image.get_rect()
        #self.rect[0] = WINDOW_SIZE[0]
        #self.rect[1] = random.randint(90, WINDOW_SIZE[1]-90)
        self.speed = 2 + random.random() * 3
        # random.random() -> Gera um valor random de 0 a 1

    def update(self):
        self.rect[0] -= self.speed

        if self.rect[0] < -100:
            self.kill()