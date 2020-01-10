import pygame
import sys
import random
from enemy import Enemy
from killer import Killer
from shot import Shot


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_shot = Shot(shots_group, WINDOW_SIZE)
                new_shot.rect.center = player.rect.center


# Define display
W, H = 1280, 720
WINDOW_SIZE = [W, H]

# Setup pygame
pygame.init()
clock = pygame.time.Clock();
tick_timer = 100
display = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("The Invasion of Lolis")
icon = pygame.image.load("data/images/icon.png")
pygame.display.set_icon(icon)
FPS = 60

# Background
bg_imgs = []
for x in range(5):
    bg_imgs.append(pygame.image.load("data/images/background/layers/parallax-" + str(x) + ".png").convert_alpha())
    bg_imgs[x] = pygame.transform.scale(bg_imgs[x], WINDOW_SIZE)

bg_velocity = [.1, .2, .5, .9, 1.8]
bg_x = [0, 0, 0, 0, 0]

# Enemy
enemy_group = pygame.sprite.Group()

# Killer
killer_group = pygame.sprite.Group()

# Shot
shots_group = pygame.sprite.Group()

player = Killer(killer_group, WINDOW_SIZE)

# test1.rect[0] = WINDOW_SIZE[0]

# Main Loop
while True:
    events()
    # Draw background
    for x in range(len(bg_imgs)):
        rel_x = bg_x[x] % bg_imgs[x].get_rect().width
        display.blit(bg_imgs[x], (rel_x - bg_imgs[x].get_rect().width, 0))
        if rel_x < W:
            display.blit(bg_imgs[x], (rel_x, 0))
        else:
            bg_x[x] = bg_velocity[x]
        bg_x[x] -= bg_velocity[x]

    tick_timer += 1
    if tick_timer > 60:
        tick_timer = 0
        # 40% de chance de probabilidade
        if random.random() < 0.4:
            new_enemy = Enemy(enemy_group)
            x = WINDOW_SIZE[0]
            y = random.randint(90, WINDOW_SIZE[1] - 90)
            new_enemy.rect.move_ip(x, y)

    shots_group.update()
    killer_group.update()
    enemy_group.update()

    collisions = pygame.sprite.spritecollide(player, enemy_group, False)
    if collisions:
        print("GG")

    hits = pygame.sprite.groupcollide(shots_group, enemy_group, True, True);

    shots_group.draw(display)
    killer_group.draw(display)
    enemy_group.draw(display)
    # Update Display
    pygame.display.update()
    # Framerate
    clock.tick(FPS)
