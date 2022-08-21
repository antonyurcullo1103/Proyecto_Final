# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 21:25:52 2022

@author:
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""
import unittest
import pandas as pd

from manejadorimagenes import categoria as cat


class TestCategoriaUnittest(unittest.TestCase):
    def test_get_name(self):
        """

        Test que la creacion de una nueva clase Categoria inicializando con el 
        nombre es correcta

        """
        nombre = "Categoria Testeo"
        cat_test = cat.Categoria(nombre, "folder path")
        self.assertEqual(cat_test.get_name(), nombre)

    def test_get_folder_path(self):
        """

        Test que la creacion de una nueva clase Categoria inicializando con el 
        path es correcta

        """
        nombre = "Categoria Testeo"
        folder_path = "Folder Path de Testeo"
        cat_test = cat.Categoria(nombre, folder_path)
        self.assertEqual(cat_test.get_folder_path(), folder_path)
