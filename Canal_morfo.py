# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 10:59:41 2016

@author: douglas
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

plt.close('all')


pathname = 'C:/Users/douglas.MENTAWAII/Documents/Dr NEMES/NEMES/NEMES/TESE\DADOS/CANAL DE ONDAS - URUGUAY/'



Tabela = Metodo_decomposicao_harmonica_Execicios.xls




H = 0.5 #:0.5:4;

Ho = H # Altura da onda incidente
hb = Ho/1 # profundidade do recife, altura da superficie até o fundo onde está o REEF;
Sb = 0.5 # profundidade da crista do REEF
Lb = 200; # largura longshore do REEF 
A = 0.161; # parâmetro A m^1/3



Quebra = hb/Ho
#Relat = 2*log(((Sb/hb)^(3/2))*((Lb/hb)^2)*(((A)^3)/hb)^0.5) +0.65

Relat = ((Sb/hb)^(3/2))*((Lb/hb)^2)*(((A)^3)/hb)^0.5

plot(Relat,Quebra)


# ASR

Y = 1 %shoreline response
B = 63 % Largura da estrutura

Sa = 175 % Crista do reef até duna
SZW = 50% largura da zona de surf

Q = Y./B
P = Sa/SZW
