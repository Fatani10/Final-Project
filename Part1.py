# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:26:36 2019

@author: Patanian10
"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd 

#part 1 store as NumPy array 
coordinates = xlrd.open_workbook(r"C:\Users\Patanian10\Desktop\Final\Coordinates.xlsx")
distancematrix = xlrd.open_workbook(r"C:\Users\Patanian10\Desktop\Final\distancematrix.xls")

note1 = coordinates.sheet_by_index(0)
note2 = distancematrix.sheet_by_index(0)