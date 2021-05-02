# -*- coding: UTF-8 -*-

'''

'''

import os
import pandas as pd
import numpy as np
import matplotlib.pylab as pl
import espec

pl.close('all')

pathname = os.environ['HOME'] + '/Dropbox/nemes/dados/ADCP_Reef_Reserva/20151221_2.2_11s/Advs/ADV_V/'
#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20151221_2.2_11s/Advs/ADV_V/'


dd = pd.read_table(pathname + 'ADV_V_corrente_21_12_2015.dat',sep='\s*',header=None, usecols=(0,2,3,4,14), names=['ens','vx','vy','vz','pr'])

dd['date'] = pd.date_range('2015-12-21 07:30',periods=len(dd), freq='250ms')

dd = dd.set_index('date')

stop

#freq de amostragem
fs = 4
nfft = 2048 / 1

#numero de amostras
a=np.unique(dd.ens)[:-1]

#hora de coleta
#hora = ['0745','0819','0853','0927','1001','1035','1109','1143','1218','1252','1326','1400','1434','1508','1542','1617','1651','1725','1759','1833','1907'][:-1]
hora = (len(dd))
dd1 = {}
epr = {}
evx = {}
evy = {}
evz = {}

#separa os dados e calcula os espectros
for i in range(len(a)):
    dd1[hora[i]] = dd.ix[pl.find(dd.ens == a[i]),:]
    epr[hora[i]] = espec.espec1(dd1[hora[i]].pr,nfft,fs)
    evx[hora[i]] = espec.espec1(dd1[hora[i]].vx,nfft,fs)
    evy[hora[i]] = espec.espec1(dd1[hora[i]].vy,nfft,fs)
    evz[hora[i]] = espec.espec1(dd1[hora[i]].vz,nfft,fs)


pl.figure()

cont = 0
for i in range(0,len(a),1):
    cont += 5
    pl.subplot(1,4,1)
    pl.plot(epr[hora[i]][:,0],cont+epr[hora[i]][:,1])
    pl.xlim(0,0.2)#, pl.ylim(0,35)
    pl.xlabel('Frequency (Hz)')
    pl.ylabel('Spectral Density (m2/Hz')
    pl.title('Pressure')
    pl.grid(axis)
    pl.subplot(1,4,2)
    pl.plot(evx[hora[i]][:,0],cont+evx[hora[i]][:,1])
    pl.xlim(0,0.2)#, pl.ylim(0,35)
    pl.title('Longshore Velocity Spectra Vx')
    pl.grid(axis)    
    pl.subplot(1,4,3)
    pl.plot(evy[hora[i]][:,0],cont+evy[hora[i]][:,1])
    pl.xlim(0,0.2)#, pl.ylim(0,25)
    pl.title('Crosshore Velocity Spectra Vy')
    pl.grid(axis)
    pl.subplot(1,4,4)
    pl.plot(evz[hora[i]][:,0],cont+evz[hora[i]][:,1])
    pl.xlim(0,0.2)#, pl.ylim(0,35)
    pl.title('Up Velocity Spectra Vz')
    pl.grid(axis)


# pl.figure()

# pl.plot(evy[hora[0]][:,0],0+evy[hora[0]][:,1])
# pl.plot(evy[hora[1]][:,0],2+evy[hora[1]][:,1])
# pl.plot(evy[hora[2]][:,0],4+evy[hora[2]][:,1])


pl.show()