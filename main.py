# Doc Pygame:   https://www.pygame.org/docs/
# Sounds:       https://opengameart.org/
# Sprites:      https://www.pixilart.com/
import pygame
pygame.init()
display = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Jogo de corno 2D")

# Sprites
spriteGroup = pygame.sprite.Group()

monster = pygame.sprite.Sprite(spriteGroup)
monster.image = pygame.image.load("data/Images/xexeca.png").convert_alpha()
piru = pygame.sprite.Sprite(spriteGroup)
piru.image = pygame.image.load("data/Images/piru.png").convert_alpha()
# Changing image scale
monster.image = pygame.transform.scale(monster.image, [120, 120])
monster.rect = monster.image.get_rect()
piru.image = pygame.transform.scale(piru.image, [120, 120])
piru.rect = piru.image.get_rect()
# Objects
rect = pygame.Rect(540, 310, 300, 50)
speed = 10

# Sounds
sound = pygame.mixer.Sound("data/Sounds/laserpew.ogg")

clock = pygame.time.Clock();
gameLoop = True

while gameLoop:
    # Framerate
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound.play()
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
    # Get inputs w, a, s and d 
    keys = pygame.key.get_pressed();
    if keys[pygame.K_w]:
        monster.rect[1] -= speed
    if keys[pygame.K_a]:
        monster.rect[0] -= speed
    if keys[pygame.K_s]:
        monster.rect[1] += speed
    if keys[pygame.K_d]:  
        monster.rect[0] += speed

    if keys[pygame.K_UP]:
        piru.rect[1] -= speed
    if keys[pygame.K_LEFT]:
        piru.rect[0] -= speed
    if keys[pygame.K_DOWN]:
        piru.rect[1] += speed
    if keys[pygame.K_RIGHT]:  
        piru.rect[0] += speed
    

    # Draw...
    display.fill([10, 10, 10])
    pygame.draw.rect(display, [0, 0, 255], rect);
    
    spriteGroup.update()
    spriteGroup.draw(display)

    # Update Display
    pygame.display.update()