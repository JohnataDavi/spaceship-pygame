# https://www.pygame.org/docs/
import pygame
pygame.init()
display = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Jogo de corno 2D")

# Objects
rect = pygame.Rect(540, 310, 200, 100)

clock = pygame.time.Clock();
gameLoop = True
speed = 10
while gameLoop:
    # Framerate
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        '''
        elif event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_w:
                rect[1] -= 50
            if  event.key == pygame.K_a:
                rect[0] -= 50
            if  event.key == pygame.K_s:
                rect[1] += 50
            if  event.key == pygame.K_d:
                rect[0] += 50
        '''
    keys = pygame.key.get_pressed();
    if keys[pygame.K_w]:
        rect[1] -= speed
    if keys[pygame.K_a]:
        rect[0] -= speed
    if keys[pygame.K_s]:
        rect[1] += speed
    if keys[pygame.K_d]:  
        rect[0] += speed
    # Draw...
    display.fill([10, 10, 10])
    pygame.draw.rect(display, [0,0,255], rect);
    pygame.display.update()