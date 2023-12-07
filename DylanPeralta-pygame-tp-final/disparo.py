import pygame as pg
from config import *
from sonidos import *

class Disparo(pg.sprite.Sprite):
    def __init__(self, x, y, direccion):
        super().__init__()
        self.image = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/disparo/disparo.png')
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.direccion = direccion
        self.velocidad = 5 
        

    def reproducir_sonido_disparo(self):
        sound_manager = SoundManager()
        sound_manager.play_shoot_sound()

    def obtener_rectangulo_disparo(self):
        return self.rect

    def update(self):
        if self.direccion == 'Derecha':
            self.rect.left = self.rect.left + self.velocidad

        elif self.direccion == 'Izquierda':
            self.rect.left = self.rect.left - self.velocidad
            
        
        

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)
        pg.draw.rect(pantalla, (0, 255, 0), self.rect, 2)