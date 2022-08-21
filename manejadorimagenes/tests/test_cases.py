# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 18:44:47 2022

@author:
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""


import unittest

import test_categoria
import test_imagen
import test_diagnostico_rayosx


suite = unittest.TestLoader().loadTestsFromTestCase(
    test_categoria.TestCategoriaUnittest)
_ = unittest.TextTestRunner().run(suite)


suite = unittest.TestLoader().loadTestsFromTestCase(test_imagen.TestImagenUnittest)
_ = unittest.TextTestRunner().run(suite)


suite = unittest.TestLoader().loadTestsFromTestCase(
    test_diagnostico_rayosx.TestDiagnosticoRayosXUnittest)
_ = unittest.TextTestRunner().run(suite)
