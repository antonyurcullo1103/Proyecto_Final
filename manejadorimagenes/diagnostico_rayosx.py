# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:25:52 2022

@author: 
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""
from imagen import Imagen
from categoria import Categoria


class DiagnosticoRayosX:
    """
    Clase 'DiagnosticoRayosX' para almacenar objetos de tipo imagen.
    """

    categorias: (Categoria, Imagen) = dict()

    def __init__(self):
        """
        La función init es la función constructor que nos permite definir 
        valores para los atributos de una instancia de la clase.

        Returns
        -------
        None.

        """

    def registrar_imagen(self, full_path):
        for k in self.categorias:
            if (k.get_folder_path() in full_path):
                nueva_imagen = Imagen(full_path)
                self.categorias[k].append(nueva_imagen)
                break

    def editar_imagen(self, imagen_modificada: Imagen):
        full_path = imagen_modificada.get_full_path()
        for k in self.categorias:
            if (k.get_folder_path() in full_path):
                for li in self.categorias[k]:
                    if (li.get_full_path() == full_path):
                        self.categorias[k].remove[li]
                        self.categorias[k].append(imagen_modificada)
                        break
                break

    def eliminar_imagen(self, full_path):
        for k in self.categorias:
            if (k.get_folder_path() in full_path):
                for li in self.categorias[k]:
                    if (li.get_full_path() == full_path):
                        self.categorias[k].remove[li]
                        break
                break

    def registrar_categoria(self, name, folder_path):
        """
        Permite añadir una nueva categoria si la llave no existe aún.

        Parameters
        ----------
        name : str
            Nombre de la categoria.
        folder_path : str
            Ruta completa del folder donde estan las imágenes.

        Returns
        -------
        None.

        """
        nueva_cat = Categoria(name, folder_path)
        hasKey = False
        for k in self.categorias:
            if (k.get_name() == name):
                hasKey = True
                break

        if (not(hasKey)):
            self.categorias[nueva_cat] = list()
            
        print(len(self.categorias))

    def eliminar_categoria(self, name):
        """
        Elimina una categoria por nombre que es la llave.

        Parameters
        ----------
        name : str
            Nombre de la categoria.

        Returns
        -------
        None.

        """
        for k in self.categorias:
            if (k.get_name() == name):
                self.categorias.pop(k)
                break

    def get_categorias(self):
        """
        Retorna las categorias.

        Returns
        -------
        dict
            Las categorias con nombre y ruta del folder.

        """
        return list(self.categorias.keys())

"""
drx = DiagnosticoRayosX()
drx.registrar_categoria("COVID-19", "..//COVID-19_Radiography_Dataset//COVID//")
drx.registrar_categoria("Normal", "..//COVID-19_Radiography_Dataset//Normal//")
drx.eliminar_categoria("COVID-19")
print(drx.get_categorias()[0].get_name())
"""