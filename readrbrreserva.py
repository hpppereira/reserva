'''
Processamento dos dados do sensor de pressao RBR
na laje do sheraton no periodo de novembro/2016

AtmosMarine

'''

import os
import pandas as pd
import numpy as np
import matplotlib.pylab as pl
from waveproc import WaveProc

pathname = os.environ['HOME'] + '/Dropbox/atmosmarine/data/lajesheraton/Swell_reserva_201611/'

filename = 'Swell_reserva_201611_data.txt'

dd = pd.read_table(pathname + filename, sep=',', header=0, names=['date', 'pr', 'spr', 'dth'], index_col='date', parse_dates=True)

w = WaveProc(pathname)

w.n1 = dd.pr.values - dd.pr.mean()
w.t = np.arange(len(w.n1))
w.dt = 
w.h = 3

w.timedomain()
