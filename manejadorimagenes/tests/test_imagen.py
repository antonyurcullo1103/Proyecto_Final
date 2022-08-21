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

from manejadorimagenes import imagen as img


class TestImagenUnittest(unittest.TestCase):
    def test_get_metadata(self):
        """

        Test para revisar la generacion de metadata de una imagen

        """
        img_path = "TestImagen.png"
        img_test = img.Imagen(img_path)
        img_test.generate_metadata()
        # check the image has at least the size attribute with values
        self.assertNotEqual(img_test.get_size(), 0)
        # now check if the filename is set
        self.assertNotEqual(img_test.get_filename(), "")
