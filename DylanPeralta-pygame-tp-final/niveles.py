from player import *
from Enemigo_dos import *
from Controles import *
from sprite import *
from Monedas import *

from plataformas import *
from menu import *
from config import*


class Nivel1:
    def __init__(self):
        self.jugador = Jugador(coordenada_x=100, coordenada_y=ALTO_PANTALLA - 100)
        self.enemigos = [Enemigo(coordenada_x=300, coordenada_y=ALTO_PANTALLA - 100), Enemigo(coordenada_x=500, coordenada_y=ALTO_PANTALLA - 100)]
        self.monedas = [Monedas(coordenada_x=200, coordenada_y=ALTO_PANTALLA - 150), Monedas(coordenada_x=400, coordenada_y=ALTO_PANTALLA - 150)]
        self.plataformas_tierra = [Plataforma_tierra(coordenada_x=0, coordenada_y=ALTO_PANTALLA - 50),Plataforma_tierra(coordenada_x=200, coordenada_y=ALTO_PANTALLA - 150)]
        self.plataformas_piedra = [Plataforma_piedra(coordenada_x=400, coordenada_y=ALTO_PANTALLA - 250),Plataforma_piedra(coordenada_x=600, coordenada_y=ALTO_PANTALLA - 350)]

    def update(self, delta_ms):
        self.jugador.actualizar(delta_ms)  # Actualizar jugador

        # Lógica de colisiones entre jugador y enemigos
        for enemigo in self.enemigos:
            if self.jugador.rectangulo_player.colliderect(enemigo.rectangulo):
                # Realizar acciones cuando hay colisión entre jugador y enemigos (p. ej., disminuir vidas, reiniciar nivel, etc.)
                pass

    def draw(self, pantalla):
        self.jugador.dibujar(pantalla)
        for enemigo in self.enemigos:
            enemigo.dibujar(pantalla)
        for moneda in self.monedas:
            moneda.dibujar(pantalla)
        for plataforma in self.plataformas_tierra + self.plataformas_piedra:
            plataforma.dibujar_plataforma_tierra(pantalla)


# class Nivel2:
#     def __init__(self):
#         # Configuración de elementos para el nivel 2

#     def update(self, delta_ms):
#         # Lógica de actualización

#     def draw(self, pantalla):
#         # Lógica de dibujo


# class Nivel3:
#     def __init__(self):
#         # Configuración de elementos para el nivel 3

#     def update(self, delta_ms):
#         # Lógica de actualización

#     def draw(self, pantalla):
#         # Lógica de dibujo


# class Nivel4:
#     def __init__(self):
#         # Configuración de elementos para el nivel 4

#     def update(self, delta_ms):
#         # Lógica de actualización

#     def draw(self, pantalla):
#         # Lógica de dibujo