
# from menu_lvl import level_selection
from opciones import *
from menu_lvl import *
from COLORES import *
from config import *
from nivel_1 import *
game_active = False

mostrar_ranking = False
boton_ranking_clickeado = False

class Menu:

    def main_menu():
        global game_active
        global mostrar_ranking 
        global boton_ranking_clickeado
        icon_y_titulo()
        # musica_level_uno()
        
        while True:
            
            imagen_menu = pg.image.load('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/elementos_juego/imagenes/botones_menus/imagen_menu.png')
            PANTALLA.blit(imagen_menu,(0,0))
            texto_menu('Menú Principal', pg.font.Font(None, 100), BLACK, PANTALLA,700, 100)
            mx, my = pg.mouse.get_pos()

            button_start = pg.Rect(810, 790, 230, 40)
            button_settings = pg.Rect(810, 840, 230, 40)
            button_ranking = pg.Rect(810, 890, 230, 40)
            button_exit = pg.Rect(810, 940, 230, 40)

            if button_start.collidepoint((mx, my)):
                if pg.mouse.get_pressed()[0]:
                    level_selection()

                pg.draw.rect(PANTALLA, BLACK, button_start)
            else:
                pg.draw.rect(PANTALLA, RED, button_start)

            if button_settings.collidepoint((mx, my)):
                if pg.mouse.get_pressed()[0]:
                    settings()

                pg.draw.rect(PANTALLA, BLACK, button_settings)
            else:
                pg.draw.rect(PANTALLA, RED, button_settings)
            
            if button_ranking.collidepoint((mx, my)):
                if pg.mouse.get_pressed()[0]:
                    mostrar_ranking = not mostrar_ranking
                if mostrar_ranking:
                    cuadro_ranking = pg.Rect(200, 50, 600, 500)  
                    pg.draw.rect(PANTALLA, BLACK, cuadro_ranking)  
                    resultados = obtener_ranking()
                    forma_texto = pg.font.Font(None, 36)
                    pos_y = 70  
                    for i, resultado in enumerate(resultados, 1):
                        if i > 10: 
                            break
                        nombre = resultado[0]
                        puntuacion = resultado[1]
                        texto = f"{i}. {nombre} - Puntuación: {puntuacion}"
                        texto_renderizado = forma_texto.render(texto, True, WHITE)
                        PANTALLA.blit(texto_renderizado, (250, pos_y))  
                        pos_y += 40
                pg.draw.rect(PANTALLA, BLACK, button_ranking)
            else:
                pg.draw.rect(PANTALLA, RED, button_ranking)
                
            if button_exit.collidepoint((mx, my)):
                if pg.mouse.get_pressed()[0]:
                    pg.quit()
                    
                pg.draw.rect(PANTALLA, BLACK, button_exit)
            else:
                pg.draw.rect(PANTALLA, RED, button_exit)

            texto_menu('Iniciar Juego', pg.font.Font(None, 36), WHITE , PANTALLA, 830, 800)
            texto_menu('Configuraciones', pg.font.Font(None, 36), WHITE , PANTALLA, 830, 850)
            texto_menu('Ranking', pg.font.Font(None, 36), WHITE , PANTALLA, 830, 900)
            texto_menu('Salir', pg.font.Font(None, 36), WHITE , PANTALLA, 830, 950)
            

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            
                # if game_active:
                #     Inicio.game()

            pg.display.update()
            clock.tick(FPS)

    if __name__ == '__main__':
        main_menu()