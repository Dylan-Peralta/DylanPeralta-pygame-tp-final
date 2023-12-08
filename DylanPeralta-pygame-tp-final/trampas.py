from sprite import Auxiliar
import pygame as pg
from config import (ANCHO_PANTALLA, ALTO_PANTALLA)
from COLORES import *

class Trampas:
    
    def __init__(self, coordenada_x, coordenada_y, ancho, alto):
        self.__trampas = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/entorno/trampas/trampa.png') 
        self.__rect = self.__trampas.get_rect()
        self.__rect.centerx = coordenada_x
        self.__rect.centery = coordenada_y
        
        self.__ancho_trampa = ancho
        self.__alto_trampa = alto

        self.rect_visible = pg.Rect(coordenada_x-5, coordenada_y-5, ancho-50, alto-200)

        self.rect_invisible = self.__rect

        self.__ancho_trampa = self.__trampas.get_width()
        self.__alto_trampa = self.__trampas.get_height()
        

    def obtener_rectangulo_trampa(self):
        return pg.Rect(self.__rect.centerx, self.__rect.centery, self.__ancho_trampa, self.__alto_trampa)

    def obtener_rectangulo_colision(self):
        return self.__rect


    def dibujar_trampa_tierra(self, pantalla: pg.surface.Surface):
        pantalla.blit(self.__trampas, (self.__rect.x, self.__rect.y))
        pg.draw.rect(pantalla, BLUE, self.rect_visible)
        pg.draw.rect(pantalla, RED, self.rect_invisible,5)
        
        

    