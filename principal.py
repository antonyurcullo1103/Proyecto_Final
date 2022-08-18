# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:24:57 2022

@author: 
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""

# Import packages
from manejadorimagenes.imagen import Imagen
from manejadorimagenes.diagnostico_rayosx import DiagnosticoRayosX

# Probando la clase Imagen
my_image = Imagen("COVID-19_Radiography_Dataset//Normal//images//Normal-1.png")
my_image.generate_metadata()
print(my_image.__str__())
print(my_image.get_format())

# cargado del dataset, lee los folder por categoria -> dataframe
# CargadorKaggle -> devolder array folders de cada categoria

drx: array = [CargadorKaggle.leng]
for 
normal = DiagnosticoRayosX(folder_name01)
covid19 = DiagnosticoRayosX(folder_name02)

# list_sub_folders: drop down list
visu = Visualizador(list_sub_folders)