import pygame

class Killer(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load("data/images/piru.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            