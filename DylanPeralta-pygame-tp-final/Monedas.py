from sprite import Auxiliar
import pygame as pg
from config import (ANCHO_PANTALLA, ALTO_PANTALLA)

class Monedas:

    def __init__(self, coordenada_x, coordenada_y, frame_rate = 100) -> None:
        self.__moneda = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/monedas/monedas.png', 9, 1, voltear=False) 
        self.__tiempo_animacion_jugador = 0
        self.__frame_rate = frame_rate
        self.__cuadro_inicial = 0
        self.__animacion_actual = self.__moneda
        self.__imagen_animacion_actual = self.__animacion_actual[self.__cuadro_inicial]  
        self.__rect = self.__imagen_animacion_actual.get_rect()
        self.__rect.y = coordenada_y
        self.__rect.x = coordenada_x
        
        self.__ancho_moneda = self.__moneda[0].get_width()
        self.__alto_moneda = self.__moneda[0].get_height()

        self.recogida = False

    def hacer_animación(self, delta_ms):
        self.__tiempo_animacion_jugador += delta_ms
        if self.__tiempo_animacion_jugador >= self.__frame_rate:
            self.__tiempo_animacion_jugador = 0
            if self.__cuadro_inicial < len(self.__animacion_actual) - 1:
                self.__cuadro_inicial += 1
            else:
                self.__cuadro_inicial = 0

    def obtener_rectangulo_moneda(self):
        return pg.Rect(self.__rect.x, self.__rect.y, self.__ancho_moneda, self.__alto_moneda)

    def update(self, delta_ms):
        self.hacer_animación(delta_ms)

    def dibujar(self, pantalla: pg.surface.Surface):
        pantalla.blit(self.__animacion_actual[self.__cuadro_inicial], self.__rect)