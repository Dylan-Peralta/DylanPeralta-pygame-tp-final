import pygame as pg
from COLORES import *
from sonidos import *
FPS = 30

#### PANTALLA ####
ANCHO_PANTALLA = 1920
ALTO_PANTALLA = 1080
PANTALLA = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))


clock = pg.time.Clock()

def texto_menu(texto, font, color, pantalla, x, y):
        textos = font.render(texto, True, color)
        texto_rectangulo = textos.get_rect()
        texto_rectangulo.topleft = (x,y)
        pantalla.blit(textos, texto_rectangulo)

#### ICONO ####
def icon_y_titulo():
    icono = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/icono/calavera.png')
    pg.display.set_icon(icono)
    pg.display.set_caption('CLAW POCHO')

#### BARRA DE VIDA ####
def dibujar_barra_vida(pantalla, jugador):
    longitud_vida = 100  # Valor máximo de la vida
    ancho_barra = 200    # Ancho de la barra de vida
    vida_actual = max(jugador.vida, 0)  # Asegurar que la vida no sea negativa
    longitud_barra = (vida_actual / longitud_vida) * ancho_barra

    # Dibujar el fondo de la barra de vida (en rojo)
    pg.draw.rect(pantalla, (RED), (1500, 25, ancho_barra, 30))

    # Dibujar la barra de vida actual (en verde)
    pg.draw.rect(pantalla, (GREEN), (1500, 25, longitud_barra, 30))  


#### MUSICA ####
def musica_level_uno():
    pg.mixer.music.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/musica/Level1.mid')
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.5)

#### FONDO ####
def fondo_uno():
    fondoo = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/entorno/level9.jpg')
    fondoo = pg.transform.scale(fondoo,(ANCHO_PANTALLA, ALTO_PANTALLA))
    PANTALLA.blit(fondoo,(0,0))

def fondo_dos():
    fondoo = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/entorno/level1.jpg')
    fondoo = pg.transform.scale(fondoo,(ANCHO_PANTALLA, ALTO_PANTALLA))
    PANTALLA.blit(fondoo,(0,0))    

def fondo_tres():
    fondoo = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/entorno/level13.jpg')
    fondoo = pg.transform.scale(fondoo,(ANCHO_PANTALLA, ALTO_PANTALLA))
    PANTALLA.blit(fondoo,(0,0)) 
    
def fondo_cuatro():
    fondoo = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/entorno/level14.jpg')
    fondoo = pg.transform.scale(fondoo,(ANCHO_PANTALLA, ALTO_PANTALLA))
    PANTALLA.blit(fondoo,(0,0))  
    
#### FIN DEL JUEGO ####
def fin_del_juego(puntaje):
    sound_manager = SoundManager()
    game_over_played = False
    fondo_game_over = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/icono/gameOver.jpg')
    fondo_game_over = pg.transform.scale(fondo_game_over,(ANCHO_PANTALLA, ALTO_PANTALLA))
    forma_texto_fin = pg.font.Font(None, 200)
    PANTALLA.blit(fondo_game_over,(0,0))
    PANTALLA.blit(forma_texto_fin.render(f'Game Over', False, 'White'), (560, 300))
    PANTALLA.blit(forma_texto_fin.render(f'Puntaje: {puntaje}', False, 'White'), (560, 600))
    
    # boton_volver = pg.Rect(ANCHO_PANTALLA/2 -220, 890, 400, 50)
    # pg.draw.rect(PANTALLA, (255, 0, 0), boton_volver)  
    # font = pg.font.Font(None, 36)
    # PANTALLA.blit(font.render(f'Volver a selección de niveles', True, (255, 255, 255)), (ANCHO_PANTALLA/2 -200, 900))

    if not game_over_played:
        sound_manager.play_game_over_sound()
        game_over_played = True

class SonidoDisparo:
    def __init__(self, ruta_sonido):
        self.sonido = pg.mixer.Sound(ruta_sonido)

    def reproducir(self):
        self.sonido.play(0)