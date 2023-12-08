from sprite import Auxiliar
import pygame as pg
from config import (ANCHO_PANTALLA, ALTO_PANTALLA)



class Enemigo:
    def __init__(self, coordenada_x, coordenada_y, velocidad = 5, vida_total = 100, gravedad = 1):
        self.__caminar_der = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/enemigo/caminar_enemigo.png', 11, 1, voltear=True)
        self.__caminar_izq = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/enemigo/caminar_enemigo.png', 11, 1, voltear=False)

        self.__velocidad_caminata = velocidad
        self.__frame_rate = 100

        self.__tiempo_movimiento_jugador = 0
        self.__tiempo_animacion_jugador = 0

        self.__cuadro_inicial = 0
        self.__animacion_actual = self.__caminar_der
        self.__imagen_animacion_actual = self.__animacion_actual[self.__cuadro_inicial]
        
        self.__ancho_del_enemigo = self.__caminar_der[0].get_width()
        self.__alto_del_enemigo = self.__caminar_izq[0].get_height()

        self.__rect = self.__imagen_animacion_actual.get_rect()
        self.__rect.y = coordenada_y
        self.__rect.x = coordenada_x
        self.__direccion = 1

        self.vida_total = vida_total
        self.vida_actual = vida_total

        self.ancho_barra_vida = 50
        self.altura_barra_vida = 5

        self.__gravedad = gravedad 
        self.velocidad_y = 0
        self.daño = -20


    def hacer_movimiento(self, delta_ms):
        self.__tiempo_movimiento_jugador += delta_ms
        if self.__tiempo_movimiento_jugador >= self.__frame_rate:
            self.__tiempo_movimiento_jugador = 0
            
            limite_izquierda = 0
            limite_derecha = ANCHO_PANTALLA - self.__rect.width

            if self.__rect.x <= limite_izquierda:
                self.__direccion = 1
            elif self.__rect.x >= limite_derecha:
                self.__direccion = -1
            self.__rect.x += self.__direccion * self.__velocidad_caminata
            
            

            if self.__direccion == -1:
                self.__animacion_actual = self.__caminar_izq
            else:
                self.__animacion_actual = self.__caminar_der 
            
    def obtener_rectangulo(self):
        return pg.Rect(self.__rect.x, self.__rect.y, self.__ancho_del_enemigo, self.__alto_del_enemigo)             

    def hacer_animación(self, delta_ms):
        self.__tiempo_animacion_jugador += delta_ms
        if self.__tiempo_animacion_jugador >= self.__frame_rate:
            self.__tiempo_animacion_jugador = 0
            if self.__cuadro_inicial < len(self.__animacion_actual) - 1:
                self.__cuadro_inicial += 1
            else:
                self.__cuadro_inicial = 0

    def aplicar_gravedad(self):
        self.velocidad_y += self.__gravedad
        self.__rect.y += self.velocidad_y
        if self.velocidad_y > 10:
            self.velocidad_y = 10        
        if self.__rect.bottom >= ALTO_PANTALLA:  
            self.__rect.bottom = ALTO_PANTALLA
            self.velocidad_y = 0 


    def update(self, delta_ms):
        self.hacer_movimiento(delta_ms)
        self.hacer_animación(delta_ms)
        self.aplicar_gravedad()

    def dibujar(self, pantalla: pg.surface.Surface):
        pantalla.blit(self.__animacion_actual[self.__cuadro_inicial], self.__rect)
        rectangulo_enemigo = self.obtener_rectangulo()
        pg.draw.rect(pantalla, (255, 0, 0), rectangulo_enemigo, 2)
        longitud_vida = self.daño  # Valor máximo de la vida
        vida_actual = max(self.vida_actual, 0)  # Asegurar que la vida no sea negativa
        longitud_barra = (vida_actual / longitud_vida) * self.ancho_barra_vida

        # Dibujar el fondo de la barra de vida (en rojo)
        pg.draw.rect(pantalla, (255, 0, 0), (self.__rect.x, self.__rect.y - 20, self.ancho_barra_vida, self.altura_barra_vida))

        # Dibujar la barra de vida actual (en verde)
        pg.draw.rect(pantalla, (0, 255, 0), (self.__rect.x, self.__rect.y - 20, longitud_barra, self.altura_barra_vida))
