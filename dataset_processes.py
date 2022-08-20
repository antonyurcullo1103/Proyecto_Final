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
import numpy as np


class DatasetProcesses:
    def __init__(self, args, kwargs):
        pass
    
    def parseDataset(self, dataset_full_name):
        """
        Read a dataset from an excel or json file given the path

        Parameters
        ----------
        dataset_full_name : TYPE
            Full path to the source file.

        Returns
        -------
        TYPE
            The dataframe returned after read the file

        """
        path, fine_name = os.path.split(dataset_full_name)
        name_without_ext, ext = os.path.splitext(fine_name)
        dataframe = ''
        if(ext == '.xls' | ext == '.xlsx'):
            dataframe = pd.read_excel(dataset_full_name)
        else:
            if (ext == '.csv'):
                dataframe = pd.read_csv(dataset_full_name)
                
        print(dataframe)
        return dataframe;