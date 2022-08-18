# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 21:25:52 2022

@author: 
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""


class Categoria:
    """
    Clase 'Categoria' para definir las categorias del dataset.
    """

    def __init__(self, name, folder_path):
        """
        La función init es la función constructor que nos permite definir 
        valores para los atributos de una instancia de la clase.

        Returns
        -------
        None.

        """
        self.name = name
        self.folder_path = folder_path

    def __str__(self):
        """
        Sobreescribir el método por defecto __str__,
        para mostrar las propiedades de esta clase.

        Returns
        -------
        str
            Metadatos.

        """
        return f"Nombre: {self.name}, Folder path: {self.folder_path}"

    # Definir las funciones para mostrar propiedades (getters)
    def get_name(self):
        return self.name

    def get_folder_path(self):
        return self.folder_path


"""    
cat = Categoria()
cat.registrar_categoria("COVID-19", "..//COVID-19_Radiography_Dataset//COVID//")
cat.registrar_categoria("Normal", "..//COVID-19_Radiography_Dataset//Normal//")
cat.eliminar_categoria("COVID-19")
print(cat.get_categorias())
"""
