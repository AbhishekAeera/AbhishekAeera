# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:06:05 2023

@author: aa23ajh
"""
import pandas as pd
import matplotlib.pyplot as plt

bcs = pd.read_csv("BCS_ann.csv")
bp= pd.read_csv("BP_ann.csv")
tsco= pd.read_csv("TSCO_ann.csv")
VOD= pd.read_csv("vod_ann.csv")

plt.Figure()

plt.Subplot(2, 2, 1)