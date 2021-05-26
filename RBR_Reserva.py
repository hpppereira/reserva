# -*- coding: UTF-8 -*-

'''

'''
import os
import numpy as np
import pylab as pl
import datetime as dt
import proconda
import jonswap
import espec
#from mpl_toolkits.mplot3d import Axes3D


pl.close('all')

reload(proconda)

#pathname = 'C:/Users/douglas.MENTAWAII/Documents/Dr NEMES/NEMES/NEMES/TESE/DADOS/CAMPO Praia da Reserva/DADOS/Perfil Praial/2015/18 05-08/ADCP/'
pathname_dn = 'C:/Users/douglas.MENTAWAII/Documents/RBR_pressao/Swell_reserva_201611/Swell_reserva_201611/'

#carrega arquivo .sen
onda = np.loadtxt(pathname_dn + 'depth_201611_data.txt')



arqs = 'depth_201611_data.txt'
        
data = [dt.datetime(int(arqs[i,2]),int(arqs[i,0]),int(arqs[i,1]),int(arqs[i,3]),int(arqs[i,4])) for i in range(len(arqs))]

h = 2.5 #profundidade 
nfft = 128 * 6 #para 1024 pontos - 16 gl #numero de dados para a fft (p/ nlin=1312: 32gl;nfft=82, 16gl;nfft=164, 8gl;nfft=328)
fs = 2 #freq de amostragem
nlin = 2048 #comprimento da serie temporal a ser processada
gl = (nlin/nfft) * 2
t = np.linspace(0,nlin*1./fs,nlin) #vetor de tempo


dd = pd.read_table(pathname_dn + arqs[0],sep='\s,*',header=None, usecols=(0,1,2,3), names=['T','Temp','P','D'])

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
