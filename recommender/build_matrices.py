# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:04:53 2020

@author: Daniel Brunnsåker
"""

import pandas as pd

data = pd.read_csv('data.txt', sep = '\t')

'''
Plan: Load into matrix, encode genres

potentially replace missing values? cluster using non-missing values, and taking mean/median of neighbors?
'''
