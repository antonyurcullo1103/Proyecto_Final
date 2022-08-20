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
    Clase 'DiagnosticoRayosX' para almacenar objetos
    de tipo imagen por categoria.
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
        """
        Registra una imagen por medio del full path con sus metadatos.

        Parameters
        ----------
        full_path : str
            Ruta absoluta de la imagen.

        Returns
        -------
        None.

        """
        # Iteramos las llaves
        for key, value in self.categorias.items():
            # Preguntamos por la categoria a traves de la ruta absoluta
            if key.get_folder_path() in full_path:
                # Creamos la instancia de la imagen
                nueva_imagen = Imagen(full_path)
                # Obtenemos sus metadatos
                nueva_imagen.generate_metadata()
                value.append(nueva_imagen)
                break

    def editar_imagen(self, imagen_modificada: Imagen):
        """
        Actualiza una imagen con sus nuevos valores.

        Parameters
        ----------
        imagen_modificada : Imagen
            Imagen modificada.

        Returns
        -------
        None.

        """
        full_path = imagen_modificada.get_full_path()
        for key, value in self.categorias.items():
            if key.get_folder_path() in full_path:
                for list_item in value:
                    if list_item.get_full_path() == full_path:
                        value.remove(list_item)
                        value.append(imagen_modificada)
                        break
                break

    def eliminar_imagen(self, full_path):
        """
        Elimina una imagen a partir de la ruta absoluta.

        Parameters
        ----------
        full_path : TYPE
            Ruta absoluta de la imagen.

        Returns
        -------
        None.

        """
        for key, value in self.categorias.items():
            if key.get_folder_path() in full_path:
                for list_item in value:
                    if list_item.get_full_path() == full_path:
                        value.remove(list_item)
                        break
                break

    def get_imagen(self, full_path):
        """
        Obtiene una imagen específica según la ruta absoluta.

        Parameters
        ----------
        full_path : str
            ruta absoluta.

        Returns
        -------
        list_item : Imagen
            Imagen encontrada en una categoria que contiene una lista de imágenes.

        """
        for key, value in self.categorias.items():
            if key.get_folder_path() in full_path:
                for list_item in value:
                    if list_item.get_full_path() == full_path:
                        return list_item

        return None

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
        has_key = False
        for k in self.categorias:
            if k.get_name() == name:
                has_key = True
                break

        if not has_key:
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
            if k.get_name() == name:
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
drx.registrar_categoria(
    "COVID-19", "..//COVID-19_Radiography_Dataset//COVID//")
drx.registrar_categoria("Normal", "..//COVID-19_Radiography_Dataset//Normal//")
drx.registrar_imagen(
    "..//COVID-19_Radiography_Dataset//Normal//images//Normal-1.png")
drx.eliminar_categoria("COVID-19")
old_imagen = drx.get_imagen(
    "..//COVID-19_Radiography_Dataset//Normal//images//Normal-1.png")
print(old_imagen.__str__())
print(drx.get_categorias()[0].get_name())
"""