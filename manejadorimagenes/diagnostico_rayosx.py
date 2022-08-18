# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:25:52 2022

@author: 
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""

class DiagnosticoRayosX:
    """
    Clase 'DiagnosticoRayosX' para almacenar objetos de tipo imagen.
    """
    
    imagenes: Imagen = list()
    

    def __init__(self, folder_name):
        """
        La función init es la función constructor que nos permite definir 
        valores para los atributos de una instancia de la clase.

        Returns
        -------
        None.

        """
        categoria = Categoria(folder_name)

    def registrar_imagen(self, full_path):
        nueva_imagen = Imagen(full_path)
        self.imagenes.append(nueva_imagen)

    def editar_imagen(self, imagen_modificada: Imagen):
        full_path = imagen_modificada.get_full_path()
        # buscar
        self.imagenes(imagen_modificada)
        
    def eliminar_imagen(self, full_path):
        # buscar
        self.imagenes(imagen_modificada)

        