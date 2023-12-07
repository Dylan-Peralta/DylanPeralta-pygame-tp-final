from sprite import Auxiliar
import pygame as pg
from config import (ANCHO_PANTALLA, ALTO_PANTALLA)
from disparo import *
class Jugador:

    def __init__(self, coordenada_x, coordenada_y, frame_rate=100, velocidad_caminata=20, velocidad_correr=50, gravedad=1,  salto=-25 ) -> None:
        self.__quieto_derecha = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/quieto.png', 8, 1, voltear=False)
        self.__quieto_izquierda = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/quieto.png', 8, 1)
        self.__caminar_derecha = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/caminar.png', 8, 1, voltear=False)
        self.__caminar_izquierda = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/caminar.png', 8, 1)
        self.__correr_derecha = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/corriendo.png', 10, 1, voltear=False)
        self.__correr_izquierda = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/corriendo.png', 10, 1)
        self.__saltar_derecha = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/salto.png', 7, 1, voltear=False)
        self.__saltar_izquierda = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/salto.png', 7, 1)
        self.__saltar_quieto_der = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/salto_quieto.png', 1, 2,voltear=False)
        self.__saltar_quieto_izq = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/salto_quieto.png', 1, 2)
        self.__disparo_derecha = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/disparo_movimiento.png', 8, 1,voltear=False)
        self.__disparo_izquierda = Auxiliar.obtener_superficie_desde_sprite('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/player/disparo_movimiento.png', 8, 1) 


        self.__mover_x = coordenada_x
        self.__mover_y = coordenada_y
        self.__velocidad_caminata = velocidad_caminata
        self.__velocidad_correr = velocidad_correr
        self.__frame_rate = frame_rate
        self.__tiempo_movimiento_jugador = 0
        self.__tiempo_animacion_jugador = 0

        self.__fuerza_salto = salto
        self.__gravedad = gravedad 
        self.__velocidad_y_jugador = 0
        self.__esta_saltando = False

        self.__ancho_del_jugador = self.__quieto_derecha[0].get_width()
        self.__alto_del_jugador = self.__quieto_derecha[0].get_height()

        self.__cuadro_inicial = 0
        self.__animacion_actual = self.__quieto_derecha
        self.__imagen_animacion_actual = self.__animacion_actual[self.__cuadro_inicial]
        self.__rect = self.__imagen_animacion_actual.get_rect()
        self.__mirando_derecha = True


        self.__rect.centerx=0
        self.__rect.centery=0
        self.vida = 100
        self.en_suelo = True
        self.bolsa_municion = []
        self.ultimo_disparo = 0 
        self.cooldown_disparo = 1000 

    def aplicar_gravedad(self, lista_plataformas):      
        self.__velocidad_y_jugador += self.__gravedad    
        self.__rect.y += self.__velocidad_y_jugador
        if self.__rect.bottom >= lista_plataformas:  
            self.__rect.bottom = lista_plataformas
            self.__velocidad_y_jugador = 0  
            self.__en_suelo = False  


    def __establecer_x_animacion_preset(self, mover_x, lista_animaciones: list[pg.surface.Surface], mirar_derecha: bool):
        self.__mover_x = mover_x
        self.__animacion_actual = lista_animaciones
        self.__mirando_derecha = mirar_derecha

    def establecer_velocidad(self, velocidad_x, velocidad_y):
        self.__velocidad_caminata = velocidad_x
        self.__gravedad = velocidad_y

    def obtener_rectangulo(self):
        return pg.Rect(self.__rect.x, self.__rect.y, self.__ancho_del_jugador, self.__alto_del_jugador)    

    def obtener_velocidad_y(self):
        return self.__velocidad_y_jugador

    def establecer_velocidad_y(self, velocidad_y):
        self.__velocidad_y_jugador = velocidad_y

    def establecer_posicion_y(self, y):
        self.__rect.y = y

    def obtener_alto(self):
        return self.__alto_del_jugador

    

    def reducir_vida(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            pass
    
    def disparo(self, direccion: str = 'Derecha'):
        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - self.ultimo_disparo > self.cooldown_disparo:
            match direccion:
                case 'Derecha':
                    mirar_derecha = True
                    # self.__establecer_x_animacion_preset(0, self.__disparo_derecha, mirar_derecha)

                    if mirar_derecha:
                        x_proyectil = self.__rect.x + self.__rect.width  
                        y_proyectil = self.__rect.y + self.__rect.height /2 - 40 
                        nuevo_proyectil = Disparo(x_proyectil, y_proyectil, direccion)  
                        self.bolsa_municion.append(nuevo_proyectil)
                        nuevo_proyectil.reproducir_sonido_disparo()
                        self.ultimo_disparo = tiempo_actual
                case 'Izquierda':
                    mirar_derecha = False
                    # self.__establecer_x_animacion_preset(-0, self.__disparo_izquierda, mirar_derecha)

                    if not mirar_derecha:
                        x_proyectil = self.__rect.x  
                        y_proyectil = self.__rect.y + self.__rect.height / 2 - 40 
                        nuevo_proyectil = Disparo(x_proyectil, y_proyectil, direccion)  
                        self.bolsa_municion.append(nuevo_proyectil)
                        nuevo_proyectil.reproducir_sonido_disparo()
                        self.ultimo_disparo = tiempo_actual

    def dibujar_proyectiles(self, pantalla):
        for proyectil in self.bolsa_municion:
            proyectil.dibujar(pantalla)

    def actualizar_proyectiles(self):
        for proyectil in self.bolsa_municion:
            proyectil.update()

    def caminar(self, direccion: str = 'Derecha'):
        match direccion:
            case 'Derecha':
                mirar_derecha = True
                self.__establecer_x_animacion_preset(self.__velocidad_caminata, self.__caminar_derecha, mirar_derecha)
            case 'Izquierda':
                mirar_derecha = False
                self.__establecer_x_animacion_preset(-self.__velocidad_caminata, self.__caminar_izquierda, mirar_derecha)


    def correr(self, direccion: str = 'Derecha'):
        match direccion:
            case 'Derecha':
                mirar_derecha = True
                self.__establecer_x_animacion_preset(self.__velocidad_correr, self.__correr_derecha, mirar_derecha)
            case 'Izquierda':
                mirar_derecha = False
                self.__establecer_x_animacion_preset(-self.__velocidad_correr, self.__correr_izquierda, mirar_derecha)

    def quedarse(self):
        if self.__animacion_actual != self.__quieto_izquierda and self.__animacion_actual != self.__quieto_derecha:
            self.__animacion_actual = self.__quieto_derecha if self.__mirando_derecha else self.__quieto_izquierda
            self.__cuadro_inicial = 0
            self.__mover_x = 0
            self.__mover_y = 0          

    def __establecer_límites_bordes(self):
        pixels_mover = 0
        if self.__mover_x > 0:
            pixels_mover = self.__mover_x if self.__rect.x < ANCHO_PANTALLA - self.__imagen_animacion_actual.get_width() else 0
        elif self.__mover_x < 0:
            pixels_mover = self.__mover_x if self.__rect.x > 0 else 0
        return pixels_mover
        
    def __establecer_límites_bordes_y(self):
        pixels_mover_y = 0
        if self.__mover_y > 0:
            pixels_mover_y = self.__mover_y if self.__rect.y < ALTO_PANTALLA - self.__imagen_animacion_actual.get_height() else 0
            
        elif self.__mover_y < 0:
            pixels_mover_y = self.__mover_y if self.__rect.y + self.__mover_y > 0 else 0

        return pixels_mover_y
        
    def hacer_movimiento(self, delta_ms):
        self.__tiempo_movimiento_jugador += delta_ms
        if self.__tiempo_movimiento_jugador >= self.__frame_rate:
            self.__tiempo_movimiento_jugador = 0
            self.__rect.x += self.__establecer_límites_bordes()
            self.__rect.y += self.__establecer_límites_bordes_y()

    def hacer_animación(self, delta_ms):
        self.__tiempo_animacion_jugador += delta_ms
        if self.__tiempo_animacion_jugador >= self.__frame_rate:
            self.__tiempo_animacion_jugador = 0
            if self.__cuadro_inicial < len(self.__animacion_actual) - 1:
                self.__cuadro_inicial += 1
            else:
                self.__cuadro_inicial = 0

    def salto(self):
        if not self.__esta_saltando:
            self.__esta_saltando = True
            self.__velocidad_y_jugador = self.__fuerza_salto
            
    

    def actualizar_salto(self, voltear ,plataformas):
        self.__velocidad_y_jugador += self.__gravedad
        self.__rect.y += self.__velocidad_y_jugador
            
        if self.__rect.bottom >= ALTO_PANTALLA:  
            self.__rect.bottom = ALTO_PANTALLA
            self.__velocidad_y_jugador = 0  
            self.__esta_saltando = False  
        if self.__rect.top <= 0:
            self.__rect.top = 0
            self.__velocidad_y_jugador = 0
            self.__esta_saltando = True
            if not self.__mover_x < 0 and voltear == True:
                self.__animacion_actual = self.__saltar_quieto_izq
            if not self.__mover_x > 0 and voltear == False:    
                self.__animacion_actual = self.__saltar_quieto_der
                if not self.__esta_saltando:
                    if self.__mover_x > 0: 
                        self.__animacion_actual = self.__saltar_derecha
                    elif self.__mover_x < 0: 
                        self.__animacion_actual = self.__saltar_izquierda
                    elif not self.__mover_x < 0 and voltear == True:
                        self.__animacion_actual = self.__saltar_quieto_izq
                    elif not self.__mover_x > 0 and voltear == False:    
                        self.__animacion_actual = self.__saltar_quieto_der
                    
            self.__cuadro_inicial += 1
            if self.__cuadro_inicial >= len(self.__animacion_actual):
                self.__cuadro_inicial = len(self.__animacion_actual) - 1


    def establecer_estado_saltando(self, estado):
        self.__esta_saltando = not estado


    def actualizar(self, delta_ms,lista_platafor):
        self.hacer_movimiento(delta_ms)
        self.hacer_animación(delta_ms)
        self.actualizar_salto(delta_ms, lista_platafor)
        self.actualizar_proyectiles()

    def dibujar(self, pantalla: pg.surface.Surface):
        self.__imagen_animacion_actual = self.__animacion_actual[self.__cuadro_inicial]
        pantalla.blit(self.__imagen_animacion_actual, self.__rect)
        pantalla.blit(self.__animacion_actual[self.__cuadro_inicial], self.__rect)
        