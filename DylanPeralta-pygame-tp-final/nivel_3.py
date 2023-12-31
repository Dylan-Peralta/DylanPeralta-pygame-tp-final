from player import *
from Enemigo_dos import *
from Controles import *
from sprite import *
from Monedas import *
from plataformas import *
from menu import *
from config import*
from disparo import *
from sonidos import *
import random
from ranking_tres import *
from trampas import *
pg.init()

def lvl_tres():
        
    #Tiempo transcurrido en el juego
    juego_iniciado = pg.time.get_ticks() 
    forma_texto_tiempo = pg.font.Font(None, 50)
    inicio_juego = True
    fin_del_juegoo = True


    #MONEDAS
    cordenadas_monedas = [
        (150,700),
        # (250,700),
        # (350,700),

        # (450,400),
        # (1075,400),
        # (1000,400),
        # (925,300),
        # (850,300),
        # (200,300),
        # (300,500),
        # (400,500),
        # (550,500),
        # (650,500),
        # (750,500),
        # (1615,500),
        # (1455,500),
        # (1300,500),

        # (750,200),
        # (905,200),
        # (1065,200)
    ]
    
    #PLAYER
    PERSONAJE = Jugador(0, 950)

    #ENEMIGO
    lista_enemigo = []
    ENEMIGO = Enemigo(random.randint(0, ANCHO_PANTALLA - 50),random.randint(0, ALTO_PANTALLA - 50))
    ENEMIGO_DOS = Enemigo(random.randint(0, ANCHO_PANTALLA - 50),random.randint(0, ALTO_PANTALLA - 50))
    ENEMIGO_TRES = Enemigo(random.randint(0, ANCHO_PANTALLA - 50),random.randint(0, ALTO_PANTALLA - 50))
    ENEMIGO_CUATRO = Enemigo(random.randint(0, ANCHO_PANTALLA - 50),random.randint(0, ALTO_PANTALLA - 50))

    lista_enemigo.append(ENEMIGO)
    lista_enemigo.append(ENEMIGO_DOS)
    lista_enemigo.append(ENEMIGO_TRES)
    lista_enemigo.append(ENEMIGO_CUATRO)

    #PLATAFORMA

    cordenadas_plataformas= [
                (100,820,2,5),
                (250,820,2,5),
                (400,820,2,5),

                (100,400,2,5),
                (250,400,2,5),
                (400,400,2,5),

                (750,700,2,5),
                
                (1050,700,2,5),

                
                (ANCHO_PANTALLA-200,400,2,5),
                (ANCHO_PANTALLA-350,400,2,5),
                (ANCHO_PANTALLA-490,400,2,5),

                (ANCHO_PANTALLA-200,820,2,5),
                (ANCHO_PANTALLA-350,820,2,5),
                (ANCHO_PANTALLA-490,820,2,5),

                (750,175,2,5),
                
                (1050,175,2,5)
                
    ]

    cordenadas_trampas= [
            (600,ALTO_PANTALLA-20,2,5),
            (787,ALTO_PANTALLA-20,2,5)
            ]
            
    lista_trampas = []
    for coordenada_x, coordenada_y, ancho, alto in cordenadas_trampas:
            plataforma = Trampas(coordenada_x, coordenada_y, ancho, alto)
            lista_trampas.append(plataforma)
            
    enfriamiento_colision_trampas = False
    tiempo_enfriamiento_trampas = 3000

    lista_plataformas = []
    for coordenada_x, coordenada_y, ancho, alto in cordenadas_plataformas:
        plataforma = Plataforma_tierra(coordenada_x, coordenada_y, ancho, alto)
        lista_plataformas.append(plataforma)

    lista_monedas = []
    for coordenada_x, coordenada_y in cordenadas_monedas:
        monedas = Monedas(coordenada_x, coordenada_y)
        lista_monedas.append(monedas)
    

    puntuacion = 0

    enfriamiento_colision = False
    tiempo_enfriamiento = 1500
    
    tiempo_ultimo_disparo = 1000 
    
    grupo_disparos = pg.sprite.Group()

    
    
    
    
    while inicio_juego:
        delta_ms = clock.tick(FPS)
        
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                inicio_juego = False
            elif event.type== pg.KEYDOWN:
                if event.key == pg.K_p:
                    Controles.pause(inicio_juego)        
                
        #### TIEMPO ####
        if inicio_juego == True:
            tiempo_transcurrido = pg.time.get_ticks()
            tiempo_restante = 60-((tiempo_transcurrido - juego_iniciado) // 1000)
                
            if tiempo_restante <= 0:
                nombre_jugador = input("Ingresa tu nombre: ") 
                guardar_sql(nombre_jugador, puntuacion)
                fin_del_juegoo = False

        
        #### FONDO ####
        fondo_tres()


        #### TIEMPO EN PANTALLA ####
        PANTALLA.blit(forma_texto_tiempo.render(f'Tiempo {tiempo_restante} ', False, 'White'), (20,25))
        
        #### ENEMIGOS ####
        for enemigo in lista_enemigo:
            enemigo.update(delta_ms)
            enemigo.dibujar(PANTALLA)
            
        
        #### PERSONAJE Y CONTROLES DEL MISMOO ###
        PERSONAJE.actualizar(delta_ms,lista_plataformas)
        PERSONAJE.dibujar(PANTALLA)
        PERSONAJE.actualizar_proyectiles()
        PERSONAJE.dibujar_proyectiles(PANTALLA)

        Controles.control_personaje(PERSONAJE)

        Controles.controles_volumen()
                

        #### PLATAFORMAS ###
        for plataforma in lista_plataformas:
            if isinstance(plataforma, Plataforma_tierra):  
                plataforma.dibujar_plataforma_tierra(PANTALLA)

        ### TRAMPAS ###
        for trampas in lista_trampas:
            if isinstance(trampas, Trampas):  
                trampas.dibujar_trampa_tierra(PANTALLA) 

        #### MONEDAS COLISION ###
        for monedas in lista_monedas:
            monedas.update(delta_ms)   
            monedas.dibujar(PANTALLA)

        for moneda in lista_monedas:
            if PERSONAJE.obtener_rectangulo().colliderect(moneda.obtener_rectangulo_moneda())and not moneda.recogida:
                sound_manager = SoundManager()
                moneda.recogida = True
                sound_manager.play_moneda_sound()
                puntuacion += 10 
                lista_monedas.remove(moneda)

        #### ENEMIGOS COLISION ####
        for enemigo in lista_enemigo:
            if PERSONAJE.obtener_rectangulo().colliderect(enemigo.obtener_rectangulo()):
                if not enfriamiento_colision:
                    sound_manager = SoundManager()
                    sound_manager.play_daño_personaje()
                    PERSONAJE.vida -= 10
                    if PERSONAJE.vida == 0:
                        nombre_jugador = input("Ingresa tu nombre: ") 
                        guardar_sql(nombre_jugador, puntuacion)
                        fin_del_juegoo = False
                        if fin_del_juegoo == False:
                            fin_del_juego(puntuacion)
                    enfriamiento_colision = True
                    tiempo_inicio_enfriamiento = pg.time.get_ticks()  

        if enfriamiento_colision:
            tiempo_actual = pg.time.get_ticks()
            if tiempo_actual - tiempo_inicio_enfriamiento >= tiempo_enfriamiento:
                enfriamiento_colision = False

        ######### DISPARO #############

        for x in PERSONAJE.bolsa_municion.copy():  
            x.dibujar(PANTALLA)
            x.update()
            grupo_disparos.add(x)
            for disparo in grupo_disparos.copy():  
                disparo.update()
                for enemigo in lista_enemigo:
                    if disparo.rect.colliderect(enemigo.obtener_rectangulo()):
                        daño = 20
                        enemigo.recibir_vida_recibido(daño)
                        PERSONAJE.bolsa_municion.remove(x)
                        print('Le diste a un enemigo')
                        if enemigo.vida_actual <= 0:
                            puntuacion += 100 
                            lista_enemigo.remove(enemigo)
                            print('Mataste a un enemigo')
                        grupo_disparos.remove(disparo)  
                        break

        #### PLATAFORMA COLISIONES ####
        for plataforma in lista_plataformas:
            jugador_rect = PERSONAJE.obtener_rectangulo()
            if jugador_rect.colliderect(plataforma.obtener_rectangulo_plataforma()):
                if PERSONAJE.obtener_velocidad_y() >= 0:
                    PERSONAJE.establecer_posicion_y(plataforma.obtener_rectangulo_plataforma().top + PERSONAJE.obtener_alto())
                    PERSONAJE.aplicar_gravedad(plataforma.obtener_rectangulo_plataforma().top)
                    PERSONAJE.establecer_estado_saltando(True)
                    
        #### TRAMPAS COLISIONES ####            
        for trampas in lista_trampas:
            if PERSONAJE.obtener_rectangulo().colliderect(trampas.obtener_rectangulo_trampa()):
                if not enfriamiento_colision_trampas:
                    sound_manager = SoundManager()
                    sound_manager.play_daño_personaje()
                    PERSONAJE.vida -= 5
                    if PERSONAJE.vida == 0:
                        nombre_jugador = input("Ingresa tu nombre: ") 
                        guardar_sql(nombre_jugador, puntuacion)
                        fin_del_juegoo = False
                        if fin_del_juegoo == False:
                            fin_del_juego(puntuacion)
                    enfriamiento_colision_trampas = True
                    tiempo_inicio_enfriamiento_trampas = pg.time.get_ticks()  

        if enfriamiento_colision_trampas:
            tiempo_actual = pg.time.get_ticks()
            if tiempo_actual - tiempo_inicio_enfriamiento_trampas >= tiempo_enfriamiento_trampas:
                enfriamiento_colision_trampas = False

        #### BARRA DE VIDA ####          
        dibujar_barra_vida(PANTALLA, PERSONAJE)

        PANTALLA.blit(forma_texto_tiempo.render(f'Puntaje {puntuacion} ', False, 'RED'), (1100,25))

    #### PANTALLA GAME OVER ####
        if fin_del_juegoo == False:
            fin_del_juego(puntuacion)
        
        pg.display.update()
    pg.quit()