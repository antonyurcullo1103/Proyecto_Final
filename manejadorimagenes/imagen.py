# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 21:25:52 2022

@author: 
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""

# Importar dependencias

# Para manipular rutas.
import os
# Python Imaging Library (PIL) permite la edición de imágenes directamente
# desde Python. Soporta una variedad de formatos como GIF, JPEG, PNG, etc.
from PIL import Image


class Imagen:
    """
    Clase 'Imagen' para almacenar metadatos y mostrarlos.
    """

    def __init__(self, full_path):
        """
        La función init es la función constructor que nos permite definir 
        valores para los atributos de una instancia de la clase.

        Parameters
        ----------
        full_path : str
            Ruta absoluta de la imagen.

        Returns
        -------
        None.

        """
        self.full_path = full_path
        self.filepath = ""
        self.filename = ""
        self.size = ""
        self.height = ""
        self.width = ""
        self.format = ""
        self.mode = ""
        self.palette = ""
        self.is_animate = ""
        self.frames_in_image = ""

    def generate_metadata(self):
        """
        Esta función sirve para generar los metados usando el
        directorio de la imagen.

        Returns
        -------
        None.

        """
        # Usando la librería PIL para leer la imagen.
        image = Image.open(self.full_path)

        # Extraer los metadatos básicos
        self.filepath, self.filename = os.path.split(image.filename)
        self.size = image.size
        self.height = image.height
        self.width = image.width
        self.format = image.format
        self.mode = image.mode
        self.palette = image.palette
        self.is_animate = getattr(image, "is_animated", False)
        self.frames_in_image = getattr(image, "n_frames", 1)

    def __str__(self):
        """
        Sobreescribir el método por defecto __str__,
        para mostrar todos los elementos de la metadata en texto.

        Returns
        -------
        str
            Metadatos.

        """
        return f"Filepath: {self.filepath}, Filename: {self.filename}, Size: {self.size}, Height: {self.height}, Widht: {self.width}, Format: {self.format}, Mode: {self.mode}, Palette: {self.palette}, Is aminate: {self.is_animate}, Frames in image: {self.frames_in_image}"

    # Definir las funciones para mostrar propiedades (getters)
    def get_full_path(self):
        return self.full_path

    def get_file_path(self):
        return self.filepath

    def get_filename(self):
        return self.filename

    def get_size(self):
        return self.size

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_format(self):
        return self.format

    def get_mode(self):
        return self.mode

    def get_palette(self):
        return self.palette

    def get_is_animate(self):
        return self.is_animate

    def get_frames_in_image(self):
        return self.frames_in_image


"""
# Probando la clase Imagen
my_image = Imagen("..//COVID-19_Radiography_Dataset//Normal//images//Normal-1.png")
my_image.generate_metadata()
print(my_image.__str__())
print(my_image.get_format())
"""
