# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:25:52 2022

@author:
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""

# Importar dependencias

import json
import os


class CargadorKaggle:
    """
    Clase 'CargadorKaggle' realiza una descarga del dataset y lo descomprime.
    """

    # Crear un folder para guardar las credenciales de acceso al API de Kaggle.
    KAGGLE_PATH = "./.kaggle"
    USERNAME = "antonyurcullo"
    KAGGLE_KEY = "25cac0013320ab9ac731c80ae7e13510"
    DATASET_NAME = "tawsifurrahman/covid19-radiography-database"
    ZIP_FILE = "covid19-radiography-database.zip"

    def __init__(self, folder_name):
        """
        La función init es la función constructor que nos permite definir
        valores para los atributos de una instancia de la clase.

        Parameters
        ----------
        folder_name : str
            Folder donde se realizará la descarga y descompresion del dataset.

        Returns
        -------
        None.

        """
        self.folder_name = folder_name

    def bash_command(self, script):
        """
        Ejecuta comandos de forma local usando el intérprete de bash.

        Parameters
        ----------
        script : str
            Comando a ejecutar.

        Returns
        -------
        None.

        """
        os.system("bash -c '%s'" % script)

    def uncompress(self):
        """
        Descomprime un arcivo ZIP y devuelve la ruta del dataset descompreso.

        Returns
        -------
        str
            Ruta absoluta del folder descompreso.

        """
        # Descomprimir el archivo ZIP.
        self.bash_command("unzip './" + self.folder_name + "/" +
                          self.ZIP_FILE + "' -d ./" + self.folder_name)
        # Eliminar el archivo ZIP.
        self.bash_command("rm ./" + self.folder_name + "/" + self.ZIP_FILE)
        # Obtener la ruta actual
        curr_dir = os.getcwd()
        # Añadir los folders hasta la ruta del folder descompreso
        os.chdir(os.path.join(curr_dir, self.folder_name))
        curr_dir = os.getcwd()
        os.chdir(os.path.join(curr_dir, "COVID-19_Radiography_Dataset"))

        # Devolver el folder del dataset descompreso
        return os.getcwd()

    def download(self):
        """
        Realiza la conección a Kaggle y descarga el dataset específico.
        Luego manda a descomprimir.

        Returns
        -------
        str
            Ruta absoluta del folder descompreso.

        """

        # Primero requerimos confirmar que el archivo aún no ha sido creado
        if os.path.exists(self.KAGGLE_PATH):
            self.bash_command("rm -r " + self.KAGGLE_PATH)

        # Crear el archivo JSON con las credenciales
        self.bash_command("mkdir " + self.KAGGLE_PATH)
        self.bash_command("touch " + self.KAGGLE_PATH+"/kaggle.json")

        # Definir las credentiales para acceder a Kaggle.
        # Puedes crear tu propio token y username de la API de Kaggle en https://www.kaggle.com/
        api_token = {"username": self.USERNAME,
                     "key": self.KAGGLE_KEY}

        # Crear un archivo con las credenciales, de tal forma que kaggle pueda leerlas facilmente
        with open(self.KAGGLE_PATH+'/kaggle.json', 'w') as file:
            json.dump(api_token, file)

            # Cambiar los permisos de acceso del nuevo archivo con credenciales
        self.bash_command("chmod 600 " + self.KAGGLE_PATH + "/kaggle.json")

        # Comprobar si el conjunto de datos ya se ha descargado
        if not os.path.exists(os.path.join("./", self.folder_name)):
            # Crear una nueva carpeta
            os.makedirs(self.folder_name)
        else:
            # Reemplazar carpeta previamente descargada
            self.bash_command("rm -r " + self.folder_name)
            os.makedirs(self.folder_name)

        # Descargar un dataset desde Kaggle
        self.bash_command("kaggle datasets download -d " +
                          self.DATASET_NAME + " -p " + self.folder_name)

        # Descomprimir dataset
        root_folder = self.uncompress()

        return root_folder

"""
# Probando la clase CargadorKaggle
dk = CargadorKaggle("dataset")
folder = dk.download()
print(folder)
"""
