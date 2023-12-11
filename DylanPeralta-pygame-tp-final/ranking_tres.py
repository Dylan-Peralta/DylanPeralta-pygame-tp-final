import sqlite3
import pygame as pg
from config import *
def guardar_sql(nombre_jugador,puntuacion):
    with sqlite3.connect('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/ranking.db') as conexion:
        try:
            sentencia = '''
                CREATE TABLE IF NOT EXISTS Posicion (
                    nombre TEXT,
                    puntuacion INTEGER
                )
            '''
            conexion.execute(sentencia)
            print("Tabla 'Posicion' creada correctamente")
        except sqlite3.OperationalError as e:
            print(f"Error creando tabla 'Posicion': {e}")

    with sqlite3.connect('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/ranking.db') as conexion:
        try:
            conexion.execute("INSERT INTO Posicion(nombre, puntuacion) VALUES (?, ?)", (nombre_jugador, puntuacion))
            conexion.commit()
            print(f"Datos de '{nombre_jugador}' insertados correctamente en la tabla 'Posicion'")
        except sqlite3.OperationalError as e:
            print(f"Error al insertar datos: {e}")

def obtener_ranking():
    with sqlite3.connect('C:/Users/Dylan/Desktop/DylanPeralta-pygame-tp-final/ranking.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, puntuacion FROM Posicion ORDER BY puntuacion DESC LIMIT 10")
        resultados = cursor.fetchall()
        return resultados
    
def mostrar_ranking():
        
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
        
