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

from manejadorimagenes import diagnostico_rayosx


class TestDiagnosticoRayosXUnittest(unittest.TestCase):
    def test_registrar_categoria(self):
        """

        Test el registro de una nueva categoria en el diagnostico

        """
        drx = diagnostico_rayosx.DiagnosticoRayosX()
        drx.registrar_categoria(
            "Normal", "..//COVID-19_Radiography_Dataset//Normal//")
        drx.registrar_categoria(
            "COVID-19", "..//COVID-19_Radiography_Dataset//COVID//")
        drx.registrar_categoria(
            "Normal", "..//COVID-19_Radiography_Dataset//Normal//")
        self.assertEqual(len(drx.get_categorias()), 2)

    def test_eliminar_categoria(self):
        """

        Test el registro de una nueva categoria en el diagnostico

        """
        drx = diagnostico_rayosx.DiagnosticoRayosX()
        drx.registrar_categoria(
            "Normal", "..//COVID-19_Radiography_Dataset//Normal//")
        drx.registrar_categoria(
            "COVID-19", "..//COVID-19_Radiography_Dataset//COVID//")
        drx.registrar_categoria(
            "Normal", "..//COVID-19_Radiography_Dataset//Normal//")
        self.assertEqual(len(drx.get_categorias()), 2)

        drx.eliminar_categoria("Normal")
        self.assertEqual(len(drx.get_categorias()), 1)
        # eliminar una categoria
