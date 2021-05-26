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

pl.close('all')

pathname_hp = os.environ['HOME'] + '/Dropbox/projects/reserva/dados/ADCP_Reef_Reserva/20151221/adcp/'
pathname_dn = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150720_1.65_8s/'

arqs = ['ADCP_REEF_21_12_2015.wad',
        'ADCP_20_07_2015.wad',
        'DADOS_21a22_11_2013.wad',
        'ADCP_REEF_01-07-2015.wad',
        'ADCP_REEF_29-07-2015.wad',
        'ADCP_05_08_2015.wad',
        'ADCP_REEF_10_09_2015.wad',
        'ADCP_REEF_16_09_2015.wad',
        'ADCP_REEF_14_12_2015.wad',
        'ADCP_REEF_13_01_2016.wad',
        'ADCP_REEF_28_01_2016.wad',
        'ADCP_REEF_14_12_2015.wad']

dd = pd.read_table(pathname_hp + arqs[0],sep='\s*',header=None, usecols=(0,2,5,6,7), names=['ens','pr','vx','vy','vz'])
#dd = pd.read_table(pathname_dn + arqs[0],sep='\s*',header=None, usecols=(0,2,5,6,7), names=['ens','pr','vx','vy','vz'])

#freq de amostragem
fs = 2
nfft = 2048 / 2

#numero de amostras
a=np.unique(dd.ens)[:-2]

#hora de coleta
hora = ['0745','0819','0853','0927','1001','1035','1109','1143','1218','1252','1326','1400','1434','1508','1542','1617','1651','1725','1759','1833','1907'][:-2]
#hora = ['1305','1335','1405','1435','1505','1535','1605','1635','1705','1735','1805','1835','1905','1935','2005','2035','2105','2135','2205','2235','2305','2335','0005','0035','0105','0135','0205','0235','0305','0335','0405','0435','0505','0535','0605','0635','0705','0735','0805','0835','0905','0935','1005','1035','1105','1135','1205'][2:-4]
#hora = ['0735','0750','0805','0820','0835','0850','0905','0920','0935','0950','1005','1020','1035','1050','1105','1120','1135','1150','1205','1220','1235','1250','1305','1220','1235','1250','1305','1320','1335','1350','1405','1420','1435','1450','1505','1520','1535','1550','1605','1620','1635','1650','1705','1720','1735','1750'][1:-3] #46

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

    dd1[hora[i]]['date'] = pd.date_range('2015-12-21 ' + hora[i][0:2] + ':' + hora[i][2:],periods=len(dd1[hora[i]]), freq='500ms')

# plot(dd_adv.index,dd_adv.vz)
# plot(dd1[hora[0]].date,dd1[hora[0]].vz)
# plot(dd1[hora[1]].date,dd1[hora[1]].vz)
# plot(dd1[hora[2]].date,dd1[hora[2]].vz)
# ...

#teste
# dd1['date'] = pd.date_range('2015-12-21 07:30',periods=len(dd), freq='500ms')

# dd = dd.set_index('date')

pl.figure()

cont = 0
for i in range(0,len(a),1):
    cont += 2
    pl.subplot(1,4,1)
    pl.semilogy(epr[hora[i]][:,0],cont+epr[hora[i]][:,1])
    pl.xlim(0,0.2), pl.ylim(0,45)
    pl.xlabel('Frequency (Hz)')
    pl.ylabel('Spectral Density (m2/Hz')
    pl.title('Pressure', fontname="Times New Roman Bold")
#    pl.grid(axis)
    pl.subplot(1,4,2)
    pl.semilogy(evx[hora[i]][:,0],cont+evx[hora[i]][:,1])
    pl.xlim(0,0.2), pl.ylim(0,45)
    pl.xlabel('Frequency (Hz)')
    pl.title('Longshore Velocity Spectra Vx')
#    pl.grid(axis)    
    pl.subplot(1,4,3)
    pl.semilogy(evy[hora[i]][:,0],cont+evy[hora[i]][:,1])
    pl.xlabel('Frequency (Hz)')
    pl.xlim(0,0.2), pl.ylim(0,45)
    pl.title('Crosshore Velocity Spectra Vy')
#    pl.grid(axis)
    pl.subplot(1,4,4)
    pl.semilogy(evz[hora[i]][:,0],cont+evz[hora[i]][:,1])
    pl.xlabel('Frequency (Hz)')
    pl.xlim(0,0.2), pl.ylim(0,45)
    pl.title('Up Velocity Spectra Vz')
#    pl.grid(axis)


# pl.figure()

# pl.plot(evy[hora[0]][:,0],0+evy[hora[0]][:,1])
# pl.plot(evy[hora[1]][:,0],2+evy[hora[1]][:,1])
# pl.plot(evy[hora[2]][:,0],4+evy[hora[2]][:,1])


pl.show()

# #from mpl_toolkits.mplot3d import Axes3D


# pl.close('all')

# #pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150720/'
# #pathname = os.environ['HOME'] + '/Dropbox/nemes/dados/ADCP_Reef_Reserva/20150720/'

# pathname = 'C:/Users/douglas.MENTAWAII/Documents/Dr NEMES/NEMES/NEMES/TESE/DADOS/CAMPO Praia da Reserva/DADOS/Perfil Praial/2015/30 28-01/ADCP/'

# #carrega arquivo .sen
# sen = np.loadtxt(pathname + 'ADCP_REEF_28_01_2016.sen')

# data = [dt.datetime(int(sen[i,2]),int(sen[i,0]),int(sen[i,1]),int(sen[i,3]),int(sen[i,4])) for i in range(len(sen))]

# h = 3.54 #profundidade 
# nfft = 2048 #para 1024 pontos - 16 gl #numero de dados para a fft (p/ nlin=1312: 32gl;nfft=82, 16gl;nfft=164, 8gl;nfft=328)
# fs = 2 #freq de amostragem
# nlin = 2048 #comprimento da serie temporal a ser processada
# gl = (nlin/nfft) * 2
# t = np.linspace(0,nlin*1./fs,nlin) #vetor de tempo

# #numero de testes habilitados (parametros para consistencia)
# #ntb = 9 #brutos
# #ntp = 3 #processado
# #npa = 19 #numero de parametros a serem calculados

# #lista os arquivo .wad
# lista = []
# for f in os.listdir(pathname):
# 	if f.endswith('.wad'):
# 		lista.append(f)
# #lista = np.sort(lista)[1:-1] #retira o primeiro arquivo que tem todos os .wad (eh o primeiro do sort)
# lista = np.sort(lista)[:]

# #retira o primeiro arquivo que tem todas as medicoes
# #e os dados que o adcp estava fora da agua
# ini = 0 #inicio das medicoes boas
# fim = len(lista) #ultima medicao boa

# lista=np.sort(lista)[ini:fim]
# data = np.array(data)[ini:fim]
# sen = sen[ini:fim,:]

# #ONDE ESTÃO SENDO RETIRADA A MARÉ DOS DADOS DE NIVEL (ONDAS)? FILTRO?

# #matonda:  0    1   2    3    4    5    6  7  8    9       10     11  12   13  14  15   16  17  18   19
# #         data, hs,h10,hmax,tmed,thmax,hm0,tp,dp,sigma1p,sigma2p,hm01,tp1,dp1,hm02,tp2,dp2,gam,gam1,gam2
# matonda = [] #matriz com parametros de onda
# matondap = [] #pressao - hs, tp dp
# fase_nnx = [] #valor do espec de fase para a fp
# fase_nny = [] #valor do espec de fase para a fp
# fase_nxny = [] #valor do espec de fase para a fp
# coer_nnx = [] #valor do espec de coerencia para a fp
# coer_nny = [] #valor do espec de coerencia para a fp
# coer_nxny = [] #valor do espec de coerencia para a fp

# #concatena todos os valores de vz (para hist)
# eta = np.array([])

# #concatena os espectros para fazer evolucao espectral
# evolspec = []

# dc = -1
# #loop para processar os dados
# for arq in lista:

#     dc += 1

#     print arq

#     dd = np.loadtxt(pathname + arq)
#     pr, vx, vy, vz = dd[:,[2,5,6,7]].T

#     #eta = np.concatenate((eta,vz),axis=1)

# 	#processamento no dominio do tempo
#     hs,h10,hmax,tmed,thmax = proconda.ondat(t,vz,h)

# 	#processamento no dominio da frequencia
# 	#hm0_pr, tp_pr, dp_pr, sigma1, sigma2, sigma1p, sigma2p, freq, df, k, sn_pr, snx,sny, snn, snnx, snny, snxny, snxnx, snyny, a1, b1, a2, b2, dire1_pr, dire2 = proconda.ondaf(
# 	#pr,vx,vy,h,nfft,fs) ##pressao

#     hm0, tp, dp, sigma1, sigma2, sigma1p, sigma2p, freq, df, k, sn, snx,sny, snn, snnx, snny, snxny, snxnx, snyny, a1, b1, a2, b2, dire1, dire2 = proconda.ondaf(vz,vx,vy,h,nfft,fs)
 
 
#  #calcula os espectros de pr, vz, vx e vy
#     apr = espec.espec1(pr,nfft,fs)
#     avz = espec.espec1(vz,nfft,fs)
#     avx = espec.espec1(vx,nfft,fs)
#     avy = espec.espec1(vy,nfft,fs)
 
#      #cria matriz para fazer evolucao espectral
#     evolspec.append(avy[:,1])


# 	#corrige a declinacao magnetica
#     dp = dp - 23
#     dire1 = dire1 - 23
#     dire2 = dire2 - 23

# 	#calcula o espectro de fase (fase e coerencia)
# 	#acha o indice da fp
#     indfp = pl.find(sn[:,0]==sn[sn[:,1]==max(sn[0:4,1]),0])
    
#     #stop

#     fase_nnx.append(np.real(snnx[indfp,4])[0]) #fase de heave e dspx
#     fase_nny.append(np.real(snny[indfp,4])[0]) #fase de heave e dspx
#     fase_nxny.append(np.real(snxny[indfp,4])[0]) #fase de heave e dspx

#     #indfp = 1

#     coer_nnx.append(np.real(snnx[indfp,5])[0]) #coerencia de heave e dspx
#     coer_nny.append(np.real(snny[indfp,5])[0]) #coerencia de heave e dspx
#     coer_nxny.append(np.real(snxny[indfp,5])[0]) #coerencia de heave e dspx

#     pl.figure()
#     pl.plot(apr[:,0],apr[:,1],'k')
#     pl.title(str(data[dc]))
#     pl.legend(['pr'],loc=2)
#     pl.xlim(0,0.3)
#     pl.twinx()
#     pl.plot(avx[:,0],avx[:,1],'b')
#     pl.plot(avy[:,0],avy[:,1],'r')
#     pl.plot(avz[:,0],avz[:,1],'g')
#     pl.legend(['vx','vy','vz'],loc=1)
#     pl.xlim(0,0.3)

#     pl.figure()
#     pl.plot(snxny[:,0],snxny[:,5])
#     pl.title(str(data[dc]))

#     pl.xlim(0,0.3)



# 	# #plota serie
# 	# pl.figure()
# 	# pl.plot(t,vz)
# 	# pl.title(str(data[dc]) + ' - Hs=%.1f' %hm0 + ' m ; Tp=%.1f ' %tp + 's; Dp=%i' %dp + ' gr')
# 	# pl.plot([t[0],t[-1]],[0,0],'--r',linewidth=3)
# 	# pl.axis('tight'), pl.grid()
# 	# pl.ylim(-1.2,1.2)
# 	# pl.ylabel('Vel. Z (m/s)')
# 	# pl.xlabel('Tempo (s)')
# 	# pl.savefig('fig/vz_serie_' + data[dc].strftime('%Y%m%d%H%M'))

# #    
# #    	#plota o espectro
# #    	pl.figure()
# #    	pl.subplot(211)
# #    	pl.plot(sn[:,0],sn[:,1])
# #    	#pl.plot(sn_pr[:,0],sn_pr[:,1],label='pr')
# #    	pl.title(str(data[dc]) + ' - Hs=%.1f' %hm0 + ' m ; Tp=%.1f ' %tp + ' s; Dp=%i' %dp + ' gr')
# #    	pl.grid()
# #    	pl.legend()
# #    	pl.ylabel(r'$(m/s)^{2}/Hz$',size=14)
# #    	pl.subplot(212)
# #    	pl.plot(sn[:,0],dire1)
# #    	pl.yticks(np.arange(0,360+45,45))
# #    	pl.ylim(0,360)
# #    	#pl.plot(sn_pr[:,0],dire1_pr)
# #    	pl.grid()
# #    	pl.xlabel('Freq. (Hz)')
# #    	pl.ylabel('Dir (graus)')
# #    	pl.savefig('figure_ADCP_05_08_2015/vz_espec_' + data[dc].strftime('%Y%m%d%H%M'))
# #    
# #    
# #    	#plota o espectro de cada variavel (pr, vz, vx e vy)
# #    	pl.figure()
# #    	pl.subplot(221)
# #    	pl.plot(apr[:,0],apr[:,1])
# #    	pl.title('Pressao')
# #    	pl.grid()
# #    	pl.subplot(222)
# #    	pl.plot(avz[:,0],avz[:,1])
# #    	pl.title('Vz')
# #    	pl.grid()
# #    	pl.subplot(223)
# #    	pl.plot(avx[:,0],avx[:,1])
# #    	pl.title('Vx')
# #    	pl.grid()
# #    	pl.subplot(224)
# #    	pl.plot(avy[:,0],avy[:,1])
# #    	pl.title('Vy')
# #    	pl.grid()
# #     
# #    	pl.savefig('figure_ADCP_05_08_2015/espectros4_' + data[dc].strftime('%Y%m%d%H%M'))
# #     
# #     
 
 
# 	#processamento no dominio da frequencia particionado (sea e swell)
#     hm01, tp1, dp1, hm02, tp2, dp2 = proconda.ondap(hm0,tp,dp,sn,dire1,df)

# 	#calculo do parametro gamma - LIOc
#     gam = jonswap.gamma(tp)
#     gam1 = jonswap.gamma(tp1)
#     gam2 = jonswap.gamma(tp2)

# 	#espectro de jonswap
#     s_js = jonswap.spec(hm0,tp,freq,gam)
#     s_js2 = jonswap.spec(hm02,tp2,freq,gam2)

# 	#concatena os dados
#     matonda.append([int(data[dc].strftime('%Y%m%d%H%M')),hs,h10,hmax,tmed,thmax,hm0,tp,dp,sigma1p,sigma2p,hm01,tp1,dp1,hm02,tp2,dp2,gam,gam1,gam2])

# #	matondap.append([hm0_pr,tp_pr,dp_pr])

# matonda = np.array(matonda)
# #matondap = np.array(matondap)
# #data = np.array(data)

# #eta = np.array(eta).reshape(np.size(eta),1)


# evolspec = np.array(evolspec).T


# pl.figure()
# pl.subplot(211)
# pl.plot(data,sen[:,14],'b')
# pl.grid()
# pl.twinx()
# #pl.plot(data,matonda[:,8],'r')
# pl.plot(data,coer_nnx,'r')
# pl.plot(data,coer_nny,'g')
# pl.plot(data,coer_nxny,'y')
# #pl.ylim(0,360)
# pl.subplot(212)
# pl.contour(np.arange(0,len(lista)),apr[:,0],evolspec,30)
# pl.xticks(range(0,len(lista),5),data[0:-1:5])
# pl.ylim(0,0.5)
# pl.grid()
# pl.show()

# '''
# pl.figure()
# h = pl.hist(eta,100)
# pl.axis('tight')
# pl.xlim(-1,1)
# pl.grid()
# pl.xlabel(r'$m/s$',fontsize=14)
# pl.ylabel(r'$Nu\'mero\ de\ ocorre\^ncias$',fontsize=14)
# pl.plot([0,0],[0,np.max(h[0])],'r--',linewidth=3)


# pl.figure()
# pl.plot(vz)

# pl.figure()
# pl.plot(sn[:,0],sn[:,1])

# pl.figure()
# pl.subplot(311)
# pl.plot(data,matonda[:,6],label='vz')
# #pl.plot(data,matondap[:,0],label='pr')
# pl.legend()
# pl.ylabel('Hm0 (m)')
# pl.subplot(312)
# pl.plot(data,matonda[:,7])
# #pl.plot(data,matondap[:,1])
# pl.ylabel('Tp (s)')
# pl.subplot(313)
# #pl.plot(data,matondap[:,2])
# pl.plot(data,matonda[:,8])
# pl.ylabel('Dp (graus)')

# pl.figure()
# pl.title('Espectros de Fase')
# pl.plot(data,fase_nnx,label='nnx')
# pl.plot(data,fase_nny,label='nny')
# pl.plot(data,fase_nxny,label='nxny')
# pl.ylabel('graus')

# pl.show()

# '''