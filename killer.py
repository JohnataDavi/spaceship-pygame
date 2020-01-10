import pygame

class Killer(pygame.sprite.Sprite):
    def __init__(self, group, window_size):
        super().__init__(group)
        self.WINDOW_SIZE = window_size
        self.image = pygame.image.load("data/images/piru.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = self.image.get_rect()
        self.rect[0] = 30
        self.speed = 0
        self.acceleration = .2

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed -= self.acceleration
        elif keys[pygame.K_s]:
            self.speed += self.acceleration
        else:
            self.speed *= .95

        self.rect[1] += self.speed

        if self.rect[1] < -16:
            self.rect[1] = -16
            self.speed = 0
        elif self.rect[1] > self.WINDOW_SIZE[1] - 95:
            self.rect[1] = self.WINDOW_SIZE[1] - 95
            self.speed = 0


