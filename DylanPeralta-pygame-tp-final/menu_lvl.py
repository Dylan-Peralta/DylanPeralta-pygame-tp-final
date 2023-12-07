import pygame as pg
from config import *
from menu import *
from COLORES import *
from nivel_1 import *
from nivel_2 import *
from nivel_3 import *
from nivel_4 import *


FPS = 30

def level_selection():
    while True:
        imagen_menu = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/botones_menus/imagen_menu.png')
        PANTALLA.blit(imagen_menu,(0,0))
        texto_menu('Selección de Nivel', pg.font.Font(None, 60), BLACK, PANTALLA, 220, 100)

        mx, my = pg.mouse.get_pos()

        level_1 = pg.Rect(300, 200, 100, 50)
        level_2 = pg.Rect(300, 300, 100, 50)
        level_3 = pg.Rect(300, 400, 100, 50)
        level_4 = pg.Rect(300, 500, 100, 50)
        boton_volver = pg.Rect(300, 600, 100, 50)

        if level_1.collidepoint((mx, my)):
            if pg.mouse.get_pressed()[0]:
                lvl_uno()
                
            pg.draw.rect(PANTALLA, RED, level_1)
        else:
            pg.draw.rect(PANTALLA, GREEN, level_1)

        if level_2.collidepoint((mx, my)):
            if pg.mouse.get_pressed()[0]:
                lvl_dos()  

            pg.draw.rect(PANTALLA, RED, level_2)
        else:
            pg.draw.rect(PANTALLA, GREEN, level_2)

        if level_3.collidepoint((mx, my)):
            if pg.mouse.get_pressed()[0]:
                lvl_tres() 

            pg.draw.rect(PANTALLA, RED, level_3)
        else:
            pg.draw.rect(PANTALLA, GREEN, level_3)

        if level_4.collidepoint((mx, my)):
            if pg.mouse.get_pressed()[0]:
                lvl_cuatro()  
            pg.draw.rect(PANTALLA, RED, level_4)
        else:
            pg.draw.rect(PANTALLA, GREEN, level_4)

        if boton_volver.collidepoint((mx, my)):
            if pg.mouse.get_pressed()[0]:
                return  

            pg.draw.rect(PANTALLA, RED, boton_volver)
        else:
            pg.draw.rect(PANTALLA, GREEN, boton_volver)

        texto_menu('Nivel 1', pg.font.Font(None, 35), BLACK, PANTALLA, 350, 200)
        texto_menu('Nivel 2', pg.font.Font(None, 35), BLACK, PANTALLA, 350, 300)
        texto_menu('Nivel 3', pg.font.Font(None, 35), BLACK, PANTALLA, 350, 400)
        texto_menu('Nivel 4', pg.font.Font(None, 35), BLACK, PANTALLA, 350, 500)
        texto_menu('Volver al Menú', pg.font.Font(None, 35), BLACK, PANTALLA, 320, 600)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                

        pg.display.update()
        clock.tick(FPS)

        