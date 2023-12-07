import pygame as pg

class Controles:
############## CONTROLES PERSONAJE ##############    
    def control_personaje(PERSONAJE):
        lista_teclas_presionadas = pg.key.get_pressed()
        if lista_teclas_presionadas[pg.K_d] and not lista_teclas_presionadas[pg.K_a]:
            PERSONAJE.caminar('Derecha')
            
        if lista_teclas_presionadas[pg.K_a] and not lista_teclas_presionadas[pg.K_d]:
            PERSONAJE.caminar('Izquierda')
            
        if not lista_teclas_presionadas[pg.K_a]  and not lista_teclas_presionadas[pg.K_d]:
            PERSONAJE.quedarse()
        
        if lista_teclas_presionadas[pg.K_d] and lista_teclas_presionadas[pg.K_LCTRL]:
            PERSONAJE.correr('Derecha')
            
        if lista_teclas_presionadas[pg.K_a] and lista_teclas_presionadas[pg.K_LCTRL]:
            PERSONAJE.correr('Izquierda')
            
        if lista_teclas_presionadas[pg.K_SPACE]:
            if lista_teclas_presionadas[pg.K_d] :
                PERSONAJE.salto()
            elif lista_teclas_presionadas[pg.K_a] :
                PERSONAJE.salto()
            else:
                PERSONAJE.salto()

        if lista_teclas_presionadas[pg.K_f]:
            if lista_teclas_presionadas[pg.K_d]:
                PERSONAJE.disparo('Derecha')
                print('DISPARANDO derecha')
            elif lista_teclas_presionadas[pg.K_a] :
                PERSONAJE.disparo('Izquierda')
                print('DISPARANDO izq')
        if not lista_teclas_presionadas[pg.K_a]  and not lista_teclas_presionadas[pg.K_d] and lista_teclas_presionadas[pg.K_f]:        
            PERSONAJE.disparo('Derecha')
    
    

############## CONTROLES VOLUMEN ############## 
    def controles_volumen():    
        teclas_volumen = pg.key.get_pressed()
        if teclas_volumen[pg.K_F1] and pg.mixer.music.get_volume() > 0.0:
            pg.mixer.music.set_volume(pg.mixer.music.get_volume() - 0.01)
            print('BAJA VOLUMEN')
            if pg.mixer.music.get_volume() == 0.0:
                print('VOLUMEN MINIMO')    
        if teclas_volumen[pg.K_F2] and pg.mixer.music.get_volume() < 1.0:
            pg.mixer.music.set_volume(pg.mixer.music.get_volume() + 0.01)
            print('SUBE VOLUMEN')
            if pg.mixer.music.get_volume() == 1.0:
                print('VOLUMEN MAXIMO')
        if teclas_volumen[pg.K_F3]:
            pg.mixer.music.set_volume(0.5)
        if teclas_volumen[pg.K_F4]:
            pg.mixer.music.set_volume(0.0)
            print('MUTE')
#######################################################################
    def pause(inicio_juego):
        pause = True   
        while pause:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pause = False
                    inicio_juego = False
                    print('JUEGO EN PAUSA')
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        pause = False
        
        