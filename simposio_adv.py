# -*- coding: UTF-8 -*-

'''

'''

import os
import pandas as pd
import numpy as np
import matplotlib.pylab as pl
import espec

pl.close('all')

#pathname = os.environ['HOME'] + '/Dropbox/nemes/dados/ADCP_Reef_Reserva/20151221_2.2_11s/adcp/'
#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20131121e22/ADV/'

#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150701/ADV/'

#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150720_1.65_8s/ADV_20_07_15/'

#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150729/ADV_no_REEF/'

#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150805/ADV_burst_17_e_18_bons_pois_muita_onda/'

#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150910/ADV 10_09_15/'

#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150915/ADV_16_09_15/'


#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20151221_2.2_11s/Advs/ADV_V/'

pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20160128/ADV/'

dd = pd.read_table(pathname + 'ADV_V_Corrente_28_01_16.dat',sep='\s*',header=None, usecols=(0,2,3,4,14), names=['ens','vx','vy','vz','pr'])

#freq de amostragem
fs = 2
nfft = 1024 / 4

#numero de amostras
a=np.unique(dd.ens)[2:-2]

#hora de coleta
hora = ['0745','0819','0853','0927','1001','1035','1109','1143','1218','1252','1326','1400','1434','1508','1542','1617','1651','1725','1759','1833','1907'][2:-2]
#hora = ['1400','1430','1500','1530','1600','1630','1700','1730','1800','1830','1900','1930','2000','2030','2100','2130','2200','2230','2300','2330','0000','0030','0100','0130','0200','0230','0300','0330','0400','0430','0500','0530','0600','0630','0700','0730','0800','0830','0900','0930','1000'][:-9]#41
#hora = ['0800','0845','0930','1015','1100','1145','1230','1315','1400','1445','1530','1615','1700','1745','1830','1915','2000','2045'][2:-3]
#hora = ['0730','0800','0830','0900','0930','1000','1030','1100','1130','1200','1230','1300','1330','1400','1430','1500','1530','1600','1630','1700','1730','1800','1830','1900','1930','2000','2030','2100','2130'][1:-4]
#hora = ['0730','0745','0800','0815','0830','0845','0900','0915','0930','0945','1000','1015','1030','1045','1100','1115','1130','1145','1200','1215','1230','1245','1300','1315','1330','1345','1400','1415','1430','1445','1500','1515','1530','1545','1600','1615','1630','1645','1700','1715','1730','1745','1800','1815'][4:-6]

#hora = (len(dd))
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
    cont += 1
    pl.subplot(1,4,1)
    pl.plot(epr[hora[i]][:,0],cont+epr[hora[i]][:,1])
    pl.xlim(0,0.2), pl.ylim(0,15)
    pl.xlabel('Frequency (Hz)')
    pl.ylabel('Spectral Density (m2/Hz')
    pl.title('Pressure')
    pl.grid(axis)
    pl.subplot(1,4,2)
    pl.plot(evx[hora[i]][:,0],cont+evx[hora[i]][:,1])
    pl.xlim(0,0.2), pl.ylim(0,15)
    pl.title('Longshore Velocity Spectra Vx')
    pl.grid(axis)    
    pl.subplot(1,4,3)
    pl.plot(evy[hora[i]][:,0],cont+evy[hora[i]][:,1])
    pl.xlim(0,0.2), pl.ylim(0,15)
    pl.title('Crosshore Velocity Spectra Vy')
    pl.grid(axis)
    pl.subplot(1,4,4)
    pl.plot(evz[hora[i]][:,0],cont+evz[hora[i]][:,1])
    pl.xlim(0,0.2), pl.ylim(0,15)
    pl.title('Up Velocity Spectra Vz')
    pl.grid(axis)


# pl.figure()

# pl.plot(evy[hora[0]][:,0],0+evy[hora[0]][:,1])
# pl.plot(evy[hora[1]][:,0],2+evy[hora[1]][:,1])
# pl.plot(evy[hora[2]][:,0],4+evy[hora[2]][:,1])


pl.show()