import pygame as pg
pg.init()
display = pg.display.set_mode([1280, 720])
pg.display.set_caption("Jogo de corno 2D")

gameLoop = True
while gameLoop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameLoop = False
            
    pg.display.update()