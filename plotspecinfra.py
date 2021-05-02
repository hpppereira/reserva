# -*- coding: UTF-8 -*-

'''

'''

import os
import pandas as pd
import numpy as np
import matplotlib.pylab as pl
import espec
import matplotlib as mpl
mpl.rc('font',family='Times New Roman')

#pl.close('all')

pathname_hp = os.environ['HOME'] + '/Dropbox/projects/reserva/dados/ADCP_Reef_Reserva/'
# pathname_dn = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150720_1.65_8s/'

arqs = [# 20131122/ #nao tem dado
        '20150701/ADCP_REEF_01-07-2015.wad',
        '20150720/ADCP_20_07_2015.wad',
        '20150729/ADCP_REEF_29-07-2015.wad',
        '20150805/ADCP_REEF_05-08-2015.wad',
        '20150910/ADCP_REEF_10_09_2015.wad',
        '20150915/ADCP_REEF_16_09_2015.wad',
        '20150916/ADCP_REEF_16_09_2015.wad',
        '20151014/ADCP_REEF_14_10_2015.wad',
        '20151111/ADCP_REEF_11_11_2015.wad',
        #20151120/ #nao tem dado
        '20151214/ADCP_REEF_14_12_2015.wad',
        '20151221/ADCP_REEF_21_12_2015.wad',
        '20160113/ADCP_REEF_13_01_2016.wad',
        '20160128/ADCP_REEF_28_01_2016.wad'
        ]


aa = 0
for arq in arqs: #varia os dias

    aa += 1

    dd = pd.read_table(pathname_hp + arq,sep='\s*',header=None, usecols=(0,2,5,6,7), names=['ens','pr','vx','vy','vz'])

    fs = 2     #freq de amostragem

    #numero de amostras
    a=np.unique(dd.ens)[:-2]

    dd1 = {}
    epr = {}
    evx = {}
    evy = {}
    evz = {}

    #separa os dados e calcula os espectros
    for v in range(len(a)): #varia as horas de cada dia

        dd1[str(v)] = dd.ix[pl.find(dd.ens == a[v]),:]
        nfft = int(dd1[str(v)].shape[0] / 2)
        epr[str(v)] = espec.espec1(dd1[str(v)].pr,nfft,fs)
        evx[str(v)] = espec.espec1(dd1[str(v)].vx,nfft,fs)
        evy[str(v)] = espec.espec1(dd1[str(v)].vy,nfft,fs)
        evz[str(v)] = espec.espec1(dd1[str(v)].vz,nfft,fs)

    pl.figure(figsize=(16,10))
    cont = 0
    for i in range(0,len(a),1):
        print(i)
        cont += 2
        pl.subplot(1,4,1)
        pl.semilogy(epr[str(i)][:,0],cont+epr[str(i)][:,1])
        pl.xlim(0,0.2), pl.ylim(0,45)
        pl.xlabel('Frequency (Hz)')
        pl.ylabel('Spectral Density (m^2/Hz)')
        pl.title('Pressure', fontname="Times New Roman Bold")
        pl.grid()
        pl.subplot(1,4,2)
        pl.semilogy(evx[str(i)][:,0],cont+evx[str(i)][:,1])
        pl.xlim(0,0.2), pl.ylim(0,45)
        pl.xlabel('Frequency (Hz)')
        pl.title('Longshore Velocity Spectra Vx')
        pl.grid()    
        pl.subplot(1,4,3)
        pl.semilogy(evy[str(i)][:,0],cont+evy[str(i)][:,1])
        pl.xlabel('Frequency (Hz)')
        pl.xlim(0,0.2), pl.ylim(0,45)
        pl.title('Crosshore Velocity Spectra Vy')
        pl.grid()
        pl.subplot(1,4,4)
        pl.semilogy(evz[str(i)][:,0],cont+evz[str(i)][:,1])
        pl.xlabel('Frequency (Hz)')
        pl.xlim(0,0.2), pl.ylim(0,45)
        pl.title('Up Velocity Spectra Vz')
        pl.grid()


    pl.savefig(arq[:8] + '_logy.png')

    pl.figure(figsize=(16,10))
    cont = 0
    for i in range(0,len(a),1):
        print(i)
        cont += 2
        pl.subplot(1,4,1)
        pl.plot(epr[str(i)][:,0],cont+epr[str(i)][:,1])
        pl.xlim(0,0.2), pl.ylim(0,45)
        pl.xlabel('Frequency (Hz)')
        pl.ylabel('Spectral Density (m^2/Hz)')
        pl.title('Pressure', fontname="Times New Roman Bold")
        pl.grid()
        pl.subplot(1,4,2)
        pl.plot(evx[str(i)][:,0],cont+evx[str(i)][:,1])
        pl.xlim(0,0.2), pl.ylim(0,45)
        pl.xlabel('Frequency (Hz)')
        pl.title('Longshore Velocity Spectra Vx')
        pl.grid()    
        pl.subplot(1,4,3)
        pl.plot(evy[str(i)][:,0],cont+evy[str(i)][:,1])
        pl.xlabel('Frequency (Hz)')
        pl.xlim(0,0.2), pl.ylim(0,45)
        pl.title('Crosshore Velocity Spectra Vy')
        pl.grid()
        pl.subplot(1,4,4)
        pl.plot(evz[str(i)][:,0],cont+evz[str(i)][:,1])
        pl.xlabel('Frequency (Hz)')
        pl.xlim(0,0.2), pl.ylim(0,45)
        pl.title('Up Velocity Spectra Vz')
        pl.grid()


    pl.savefig(arq[:8] + '.png')


    # pl.figure()

    # pl.plot(evy[hora[0]][:,0],0+evy[hora[0]][:,1])
    # pl.plot(evy[hora[1]][:,0],2+evy[hora[1]][:,1])
    # pl.plot(evy[hora[2]][:,0],4+evy[hora[2]][:,1])


    pl.show()
