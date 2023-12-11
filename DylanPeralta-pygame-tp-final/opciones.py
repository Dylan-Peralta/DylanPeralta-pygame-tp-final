import pygame as pg
from config import *
from menu import *
from COLORES import *

music_enabled = True  
sound_effects_enabled = True

def settings():
    global music_enabled, sound_effects_enabled
    while True:
        imagen_menu = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/botones_menus/imagen_menu.png')
        PANTALLA.blit(imagen_menu,(0,0))
        texto_menu('Configuraciones', pg.font.Font(None, 100), BLACK, PANTALLA, 650, 100)

        mx, my = pg.mouse.get_pos()

        button_back = pg.Rect(800, 450, 200, 50)
        if button_back.collidepoint((mx, my)):
            if pg.mouse.get_pressed()[0]:
                return  

            pg.draw.rect(PANTALLA, RED, button_back)
        else:
            pg.draw.rect(PANTALLA, GREEN, button_back)

        texto_menu('Volver', pg.font.Font(None, 36), BLACK, PANTALLA, 860, 460)

            
        button_music = pg.Rect(700, 200, 420, 50)
        button_sound_effects = pg.Rect(700, 300, 420, 50)

            
        if button_music.collidepoint((mx, my)):
            if pg.mouse.get_pressed()[0]:
                music_enabled = not music_enabled  

            pg.draw.rect(PANTALLA, GREEN if music_enabled else RED, button_music)
        else:
            pg.draw.rect(PANTALLA, GREEN if music_enabled else RED, button_music)

        texto_menu('Música: ' + ('Activada' if music_enabled else 'Desactivada'), pg.font.Font(None, 36), BLACK, PANTALLA, 800, 210)

            
        if button_sound_effects.collidepoint((mx, my)):
            if pg.mouse.get_pressed()[0]:
                sound_effects_enabled = not sound_effects_enabled  

            pg.draw.rect(PANTALLA, GREEN if sound_effects_enabled else RED, button_sound_effects)
        else:
            pg.draw.rect(PANTALLA, GREEN if sound_effects_enabled else RED, button_sound_effects)

        texto_menu('Efectos de Sonido: ' + ('Activados' if sound_effects_enabled else 'Desactivados'), pg.font.Font(None, 36), BLACK, PANTALLA, 720, 310)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                    

        pg.display.update()
        clock.tick(FPS)