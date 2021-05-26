'''
Aprendendo WAFO - Reserva
'''

import os
import pandas as pd
import wafo as wf
from  waveproc import WaveProc
import numpy as np

pathname = os.environ['HOME'] + '/Dropbox/reserva/dados/ADCP_Reef_Reserva/'

wad = pd.read_table(pathname + '20150916/ADCP_REEF_16_09_2015016.wad', sep='\s*', header=None, index_col=False,
		            names=['bur','coun','pres','spare','analog','vxe','vyn','vzu','amp1','amp2','amp3','ampna'])


w = WaveProc(pathname)

w.n1 = np.array(wad.pres) - wad.pres.mean()
w.n2 = wad.vxe
w.n3 = wad.vyn
w.h = wad.pres.mean() + 0.9
w.t = np.array(wad.coun)
w.dt = w.t[3] - w.t[2]
w.fs = 1/w.dt
w.nfft = 256


w.timedomain()
w.freqdomain()


