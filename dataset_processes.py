# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 23:11:03 2022

@author: 
    ADAN MAIKON TERAN JUAREZ
    ANTONY CRISTIAN URCULLO ROSALES
    VICTOR ERNESTO DE LAS MONTAÑAS ORTEGA LIJERON
    RONALD TORRICO OVANDO
"""

import os
import pandas as pd

from manejadorimagenes import categoria as cat


class DatasetProcesses:
    def __init__(self):
        pass

    def parseDataset(self, dataset_full_name) -> pd.DataFrame:
        """
        Read a dataset from an excel or json file given the path

        Parameters
        ----------
        dataset_full_name : string
            Full path to the source file.

        Returns
        -------
        TYPE
            The dataframe returned after read the file

        """
        path, fine_name = os.path.split(dataset_full_name)
        name_without_ext, ext = os.path.splitext(fine_name)
        dataframe = ''
        if(ext == '.xls' or ext == '.xlsx'):
            dataframe = pd.read_excel(dataset_full_name)
        else:
            if (ext == '.csv'):
                dataframe = pd.read_csv(dataset_full_name)

        return dataframe

    def loadCategoriesFromRootPath(self, root_path: str) -> list[cat.Categoria]:
        """
        Load all the categories that exists in the given root path

        Parameters
        ----------
        root_path : str
            Root path where our image files are stored.

        Returns
        -------
        categories : list[cat.Categoria]
            It returns an array with all the categories loaded, they are 
            returned as Categoria object.

        """
        categories = []
        for file in os.listdir(root_path):
            if file.endswith(".xlsx"):
                name_without_ext, ext = os.path.splitext(file)
                name_without_metadata, metadata_text = os.path.splitext(
                    name_without_ext)
                new_cat = cat.Categoria(
                    name_without_metadata, os.path.join(root_path, file))
                categories.append(new_cat)
        return categories

    def loadDatasetsFromRootPath(self, root_path: str) -> dict[str, pd.DataFrame]:
        """
        Load all the dataframes inside the given root path, it reads all the 
        categories and return the dataframes in a dictionary

        Parameters
        ----------
        root_path : str
            Root path where our image files are stored.

        Returns
        -------
        dataframes : dict[str, pd.DataFrame]            
            It returns an array with all the categories loaded, they are 
            returned as Categoria object..

        """
        dataframes = {}
        for file in os.listdir(root_path):
            if file.endswith(".xlsx"):
                name_without_ext, ext = os.path.splitext(file)
                name_without_metadata, metadata_text = os.path.splitext(
                    name_without_ext)
                df = self.parseDataset(os.path.join(root_path, file))
                dataframes[name_without_metadata] = df
        return dataframes

    def loadDatasetsByCategoryNames(
            self, 
            root_path: str, 
            category_names: list[str]) -> dict[str, pd.DataFrame]:
        """
        Load all the dataframes inside the given root path, it reads only the 
        categories provided in the paramenter, and return the dataframes in 
        a dictionary
        
        Parameters
        ----------
        root_path : str
            Root path where our image files are stored.
        category_names : list[str]
            DESCRIPTION.

        Returns
        -------
        dataframes : dict[str, pd.DataFrame]:                   
            It returns an array with all the categories loaded, they are 
            returned as Categoria object...

        """
        dataframes = {}
        for file in os.listdir(root_path):
            if file.endswith(".xlsx"):
                name_without_ext, ext = os.path.splitext(file)
                name_without_metadata, metadata_text = os.path.splitext(
                    name_without_ext)
                if name_without_metadata in category_names:
                    df = self.parseDataset(os.path.join(root_path, file))
                    dataframes[name_without_metadata] = df
        return dataframes
