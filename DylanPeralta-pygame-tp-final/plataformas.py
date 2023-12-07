from sprite import Auxiliar
import pygame as pg
from config import (ANCHO_PANTALLA, ALTO_PANTALLA)
from COLORES import *
class Plataforma_tierra:
    
    def __init__(self, coordenada_x, coordenada_y, ancho, alto):
        self.__plataformma = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/entorno/plataformas/tierra1.png') 
        self.__rect = self.__plataformma.get_rect()
        self.__rect.centerx = coordenada_x
        self.__rect.centery = coordenada_y
        
        self.__ancho_plataforma = ancho
        self.__alto_plataforma = alto

        self.rect_visible = pg.Rect(coordenada_x-5, coordenada_y-5, ancho-50, alto-200)

        self.rect_invisible = self.__rect

        self.__ancho_plataforma = self.__plataformma.get_width()
        self.__alto_plataforma = self.__plataformma.get_height()
        

    def obtener_rectangulo_plataforma(self):
        return pg.Rect(self.__rect.centerx, self.__rect.centery, self.__ancho_plataforma, self.__alto_plataforma)

    def obtener_rectangulo_colision(self):
        return self.__rect


    def dibujar_plataforma_tierra(self, pantalla: pg.surface.Surface):
        pantalla.blit(self.__plataformma, (self.__rect.x, self.__rect.y))
        pg.draw.rect(pantalla, BLUE, self.rect_visible)
        pg.draw.rect(pantalla, RED, self.rect_invisible,5)
        
        

class Plataforma_piedra:

    def __init__(self, coordenada_x, coordenada_y):
        self.__plataformma = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/entorno/plataformas/piedra1.png') 
        self.__rect = self.__plataformma.get_rect()
        self.__rect.y = coordenada_y
        self.__rect.x = coordenada_x

    def dibujar_plataforma_piedra(self, pantalla: pg.surface.Surface):
        pantalla.blit(self.__plataformma, (self.__rect.y,self.__rect.x))

    