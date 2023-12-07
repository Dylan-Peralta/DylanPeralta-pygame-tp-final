import pygame as pg

class SoundManager:
    def __init__(self):
        pg.init()
        self.game_over_sound = pg.mixer.Sound("C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/musica/efectos de sonido game over/fail-144746.mp3")
        self.sonido_disparo = pg.mixer.Sound('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/musica/efecto de sonido disparar/9mm-pistol-shot-6349.mp3')  
        self.sonido_moneda = pg.mixer.Sound('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/musica/Efectos de sonido monedas/collectcoin-6075.mp3')
        self.daño_personaje = pg.mixer.Sound('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/musica/Efectos de sonido de daño/umph-47201.mp3')
        self.is_muted = False  

    def play_game_over_sound(self):
        if not self.is_muted:
            self.game_over_sound.play(0)

    def play_daño_personaje(self):
        if not self.is_muted:
            self.daño_personaje.play(0)

    def play_shoot_sound(self):
        if not self.is_muted:
            self.sonido_disparo.play(0)

    def play_moneda_sound(self):
        if not self.is_muted:
            self.sonido_moneda.play(0)

    def toggle_mute(self):
        self.is_muted = not self.is_muted

    def stop_all_sounds(self):
        pg.mixer.stop()