import pygame as pg

class Auxiliar:
    @staticmethod
    def obtener_superficie_desde_sprite(ruta_img: str, columnas: int, filas: int, paso=1, voltear: bool = True) -> list[pg.surface.Surface]:
        lista_sprites = list()
        superficie_img = pg.image.load(ruta_img)
        ancho_celda = int(superficie_img.get_width() / columnas)
        alto_celda = int(superficie_img.get_height() / filas)

        for fila in range(filas):
            for columna in range(0, columnas, paso):
                eje_x = columna * ancho_celda
                eje_y = fila * alto_celda

                superficie_celda = superficie_img.subsurface(eje_x, eje_y, ancho_celda, alto_celda)

                if voltear:
                    superficie_celda = pg.transform.flip(superficie_celda, True, False)
                lista_sprites.append(superficie_celda)
        
        return lista_sprites