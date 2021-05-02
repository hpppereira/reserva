# -*- coding: utf-8 -*-
'''
Programa para processar os dados do ADCP
instalado na Praia da Reserva
Projeto LDSC

Douglas Nemes
Francisco Sudau
Henrique Pereira
Ricardo Campos

Data da ultima modificacao: 22/09/2015

Observacoes:
- concatena os dados .wad (pegar o ja concatenado)
- processamento no dominio do tempo e frequencia
- processar utilizando a serie de velocidade veritical
 e dividir por omega2 para obter o espectro de heave

#- cabecalho do 
.sen
Number of measurements                46
Number of checksum errors             0
Time of first measurement             11/11/2015 07:30:00
Time of last measurement              11/11/2015 18:50:01

Profile interval                      900 sec
Number of cells                       8
Cell size                             50 cm
Average interval                      300 sec

Blanking distance                     0.40 m
Compass update rate                   900 sec

Wave - Interval                       900 sec
Wave - Number of samples              1024
Wave - Sampling rate                  2 Hz
Wave - Cell size                      1.00 m

Coordinate system                     ENU

Current profile cell center distance from head (m)
---------------------------------------------------------------------
  1    0.90
  2    1.40
  3    1.90
  4    2.40
  5    2.90
  6    3.40
  7    3.90
  8    4.40

#####################################################################
arquivo .sen

 1   Month                            (1-12)
 2   Day                              (1-31)
 3   Year
 4   Hour                             (0-23)
 5   Minute                           (0-59)
 6   Second                           (0-59)
 7   Error code
 8   Status code
 9   Battery voltage                  (V)
10   Soundspeed                       (m/s)
11   Heading                          (degrees)
12   Pitch                            (degrees)
13   Roll                             (degrees)
14   Pressure                         (dbar)
15   Temperature                      (degrees C)
16   Analog input 1
17   Analog input 2

#####################################################################
arquivo .whd

 1   Month                            (1-12)
 2   Day                              (1-31)
 3   Year
 4   Hour                             (0-23)
 5   Minute                           (0-59)
 6   Second                           (0-59)
 7   Burst counter
 8   No of wave data records
 9   Cell position                    (m)
10   Battery voltage                  (V)
11   Soundspeed                       (m/s)
12   Heading                          (degrees)
13   Pitch                            (degrees)
14   Roll                             (degrees)
15   Minimum pressure                 (dbar)
16   Maximum pressure                 (dbar)
17   Temperature                      (degrees C)
18   CellSize                         (m)
19   Noise amplitude beam 1           (counts)
20   Noise amplitude beam 2           (counts)
21   Noise amplitude beam 3           (counts)
22   Noise amplitude beam 4           (counts)
23   AST window start                 (m)
24   AST window size                  (m)
25   AST window offset                (m)

#####################################################################
arquivo .wad

 1   Burst counter
 2   Ensemble counter
 3   Pressure                         (dbar)
 4   Spare
 5   Analog input
 6   Velocity (Beam1|X|East)          (m/s)
 7   Velocity (Beam2|Y|North)         (m/s)
 8   Velocity (Beam3|Z|Up)            (m/s)
 9   Velocity (N/A)                   (m/s)
10   Amplitude (Beam1)                (counts)
11   Amplitude (Beam2)                (counts)
12   Amplitude (Beam3)                (counts)
13   Amplitude (N/A)                  (counts)
'''

import os
import numpy as np
import pylab as pl
import datetime as dt
import proconda
import jonswap
import espec
import pandas as pd
#from mpl_toolkits.mplot3d import Axes3D


pl.close('all')

reload(proconda)


#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/'
pathname = os.environ['HOME'] + '/Dropbox/reserva/dados/ADCP_Reef_Reserva/'

lista = np.sort(os.listdir(pathname))

#pathname = 'C:/Users/douglas.MENTAWAII/Documents/Dr NEMES/NEMES/NEMES/TESE/DADOS/CAMPO Praia da Reserva/DADOS/Perfil Praial/2015/30 28-01/ADCP/'

#escolhe o dia (fazer: entrar com string de data)
dayf = lista[4]

listarq = np.sort(os.listdir(pathname + dayf))

dateparse = lambda x: pd.datetime.strptime(x,'%m %d %Y %H %M %S') 

for i in range(len(listarq)):

    if listarq[i].endswith(dayf[0:4] + '.a1'):
        a1 = pd.read_table(pathname + dayf + '/' + listarq[i], sep='\s*')

    elif listarq[i].endswith(dayf[0:4] + '.sen'):
        sen = pd.read_table(pathname + dayf + '/' + listarq[i], sep='\s*', header=None, parse_dates=[[0,1,2,3,4,5]], date_parser=dateparse,
            index_col='mo_dy_yr_hr_mn_sec',
            names=['mo','dy','yr','hr','mn','sec','er_code','st_code','bat','soudspd','head','pitch','roll','pres','temp','anin1','anin2'])

    elif listarq[i].endswith(dayf[0:4] + '.v1'):
        v1 = pd.read_table(pathname + dayf + '/' + listarq[i], sep='\s*', header=None, names=['c1','c2','c3','c4','c5','c6'])

    elif listarq[i].endswith(dayf[0:4] + '.v2'):
        v2 = pd.read_table(pathname + dayf + '/' + listarq[i], sep='\s*', header=None, names=['c1','c2','c3','c4','c5','c6'])

    elif listarq[i].endswith(dayf[0:4] + '.v3'):
        v3 = pd.read_table(pathname + dayf + '/' + listarq[i], sep='\s*', header=None, names=['c1','c2','c3','c4','c5','c6'])

    elif listarq[i].endswith(dayf[0:4] + '.whd'):
        whd = pd.read_table(pathname + dayf + '/' + listarq[i], sep='\s*', header=None, parse_dates=[[0,1,2,3,4,5]], date_parser=dateparse, 
            index_col='mo_dy_yr_hr_mn_sec',
            names=['mo','dy','yr','hr','mn','sec','burstc','nodata','celpos','bat','soudspd','head','pitch','roll','minpres',
            'maxpres','temp','celsize','namp1','namp2','namp3','namp4','astst','astsz','astof'])

    elif listarq[i].endswith(dayf[0:4] + '.wad'):
        print listarq[i]
        wad = pd.read_table(pathname + dayf + '/' + listarq[i], sep='\s*', header=None, index_col=False,
            names=['burst','count','pres','spare','analog','vxe','vyn','vzu','amp1','amp2','amp3','ampna'])


#        sen = pd.read_table(pathname + dayf + '/' + listarq[i], sep='\s*', header=None, names=['mo','dy','yr','hr','mn','sec'], parse_dates=['mo','dy'], date_parser=dateparse )


#cria vetor de tempo para onda (intercalando as amostragens)
wad['time'] = 0

cont = 0
cont1 = 0
cont2 = 0 #wad.burst.loc[wad.burst == cont].shape[0]
for i in range(len(whd)):

    cont += 1

    #tamanho do vetor da hora
    cont2 = wad.burst.loc[wad.burst == cont].shape[0] + cont2
    
    aux = pd.date_range(whd.index[i], periods=wad.burst.loc[wad.burst == cont].shape[0], freq='500ms')

    wad.time[cont1:cont2] = aux

    cont1 = cont2 

wad = wad.set_index('time')

fig = pl.figure()
ax1 = fig.add_subplot(111)
ax1.plot(wad.index, wad.pres)
ax1.plot(sen.index, sen.pres)


pl.show()




#carrega arquivo .sen
#sen = np.loadtxt(pathname + 'ADCP_20_07_2015.sen')

#sen = pd.read_table(pathname + 'ADCP_20_07_2015.sen', sep='*s') #, parse_dates=[0], date_parser=dateparse )


#df = pd.read_csv(infile, parse_dates=['datetime'], date_parser=dateparse)


data = [dt.datetime(int(sen[i,2]),int(sen[i,0]),int(sen[i,1]),int(sen[i,3]),int(sen[i,4])) for i in range(len(sen))]

h = 3.54 #profundidade 
nfft = 256 #para 1024 pontos - 16 gl #numero de dados para a fft (p/ nlin=1312: 32gl;nfft=82, 16gl;nfft=164, 8gl;nfft=328)
fs = 2 #freq de amostragem
nlin = 2048 #comprimento da serie temporal a ser processada
gl = (nlin/nfft) * 2
t = np.linspace(0,nlin*1./fs,nlin) #vetor de tempo

#numero de testes habilitados (parametros para consistencia)
#ntb = 9 #brutos
#ntp = 3 #processado
#npa = 19 #numero de parametros a serem calculados

#lista os arquivo .wad
lista = []
for f in os.listdir(pathname):
	if f.endswith('.wad'):
		lista.append(f)
#lista = np.sort(lista)[1:-1] #retira o primeiro arquivo que tem todos os .wad (eh o primeiro do sort)
lista = np.sort(lista)[:]

#retira o primeiro arquivo que tem todas as medicoes
#e os dados que o adcp estava fora da agua
ini = 0 #inicio das medicoes boas
fim = len(lista) #ultima medicao boa

lista=np.sort(lista)[ini:fim]
data = np.array(data)[ini:fim]
sen = sen[ini:fim,:]

#ONDE ESTÃO SENDO RETIRADA A MARÉ DOS DADOS DE NIVEL (ONDAS)? FILTRO?

#matonda:  0    1   2    3    4    5    6  7  8    9       10     11  12   13  14  15   16  17  18   19
#         data, hs,h10,hmax,tmed,thmax,hm0,tp,dp,sigma1p,sigma2p,hm01,tp1,dp1,hm02,tp2,dp2,gam,gam1,gam2
matonda = [] #matriz com parametros de onda
matondap = [] #pressao - hs, tp dp
fase_nnx = [] #valor do espec de fase para a fp
fase_nny = [] #valor do espec de fase para a fp
fase_nxny = [] #valor do espec de fase para a fp
coer_nnx = [] #valor do espec de coerencia para a fp
coer_nny = [] #valor do espec de coerencia para a fp
coer_nxny = [] #valor do espec de coerencia para a fp

#concatena todos os valores de vz (para hist)
eta = np.array([])

#concatena os espectros para fazer evolucao espectral
evolspec = []

dc = -1
#loop para processar os dados
for arq in lista:

    dc += 1

    print arq

    dd = np.loadtxt(pathname + arq)
    pr, vx, vy, vz = dd[:,[2,5,6,7]].T

    #eta = np.concatenate((eta,vz),axis=1)

	#processamento no dominio do tempo
    hs,h10,hmax,tmed,thmax = proconda.ondat(t,vz,h)

	#processamento no dominio da frequencia
	#hm0_pr, tp_pr, dp_pr, sigma1, sigma2, sigma1p, sigma2p, freq, df, k, sn_pr, snx,sny, snn, snnx, snny, snxny, snxnx, snyny, a1, b1, a2, b2, dire1_pr, dire2 = proconda.ondaf(
	#pr,vx,vy,h,nfft,fs) ##pressao

    hm0, tp, dp, sigma1, sigma2, sigma1p, sigma2p, freq, df, k, sn, snx,sny, snn, snnx, snny, snxny, snxnx, snyny, a1, b1, a2, b2, dire1, dire2 = proconda.ondaf(vz,vx,vy,h,nfft,fs)
 
 
 #calcula os espectros de pr, vz, vx e vy
    apr = espec.espec1(pr,nfft,fs)
    avz = espec.espec1(vz,nfft,fs)
    avx = espec.espec1(vx,nfft,fs)
    avy = espec.espec1(vy,nfft,fs)
 
     #cria matriz para fazer evolucao espectral
    evolspec.append(avy[:,1])


	#corrige a declinacao magnetica
    dp = dp - 23
    dire1 = dire1 - 23
    dire2 = dire2 - 23

	#calcula o espectro de fase (fase e coerencia)
	#acha o indice da fp
    indfp = pl.find(sn[:,0]==sn[sn[:,1]==max(sn[0:4,1]),0])
    
    #stop

    fase_nnx.append(np.real(snnx[indfp,4])[0]) #fase de heave e dspx
    fase_nny.append(np.real(snny[indfp,4])[0]) #fase de heave e dspx
    fase_nxny.append(np.real(snxny[indfp,4])[0]) #fase de heave e dspx

    #indfp = 1

    coer_nnx.append(np.real(snnx[indfp,5])[0]) #coerencia de heave e dspx
    coer_nny.append(np.real(snny[indfp,5])[0]) #coerencia de heave e dspx
    coer_nxny.append(np.real(snxny[indfp,5])[0]) #coerencia de heave e dspx

    pl.figure()
    pl.plot(apr[:,0],apr[:,1],'k')
    pl.title(str(data[dc]))
    pl.legend(['pr'],loc=2)
    pl.xlim(0,0.3)
    pl.twinx()
    pl.plot(avx[:,0],avx[:,1],'b')
    pl.plot(avy[:,0],avy[:,1],'r')
    pl.plot(avz[:,0],avz[:,1],'g')
    pl.legend(['vx','vy','vz'],loc=1)
    pl.xlim(0,0.3)

    pl.figure()
    pl.plot(snxny[:,0],snxny[:,5])
    pl.title(str(data[dc]))

    pl.xlim(0,0.3)



	# #plota serie
	# pl.figure()
	# pl.plot(t,vz)
	# pl.title(str(data[dc]) + ' - Hs=%.1f' %hm0 + ' m ; Tp=%.1f ' %tp + 's; Dp=%i' %dp + ' gr')
	# pl.plot([t[0],t[-1]],[0,0],'--r',linewidth=3)
	# pl.axis('tight'), pl.grid()
	# pl.ylim(-1.2,1.2)
	# pl.ylabel('Vel. Z (m/s)')
	# pl.xlabel('Tempo (s)')
	# pl.savefig('fig/vz_serie_' + data[dc].strftime('%Y%m%d%H%M'))

#    
#    	#plota o espectro
#    	pl.figure()
#    	pl.subplot(211)
#    	pl.plot(sn[:,0],sn[:,1])
#    	#pl.plot(sn_pr[:,0],sn_pr[:,1],label='pr')
#    	pl.title(str(data[dc]) + ' - Hs=%.1f' %hm0 + ' m ; Tp=%.1f ' %tp + ' s; Dp=%i' %dp + ' gr')
#    	pl.grid()
#    	pl.legend()
#    	pl.ylabel(r'$(m/s)^{2}/Hz$',size=14)
#    	pl.subplot(212)
#    	pl.plot(sn[:,0],dire1)
#    	pl.yticks(np.arange(0,360+45,45))
#    	pl.ylim(0,360)
#    	#pl.plot(sn_pr[:,0],dire1_pr)
#    	pl.grid()
#    	pl.xlabel('Freq. (Hz)')
#    	pl.ylabel('Dir (graus)')
#    	pl.savefig('figure_ADCP_05_08_2015/vz_espec_' + data[dc].strftime('%Y%m%d%H%M'))
#    
#    
#    	#plota o espectro de cada variavel (pr, vz, vx e vy)
#    	pl.figure()
#    	pl.subplot(221)
#    	pl.plot(apr[:,0],apr[:,1])
#    	pl.title('Pressao')
#    	pl.grid()
#    	pl.subplot(222)
#    	pl.plot(avz[:,0],avz[:,1])
#    	pl.title('Vz')
#    	pl.grid()
#    	pl.subplot(223)
#    	pl.plot(avx[:,0],avx[:,1])
#    	pl.title('Vx')
#    	pl.grid()
#    	pl.subplot(224)
#    	pl.plot(avy[:,0],avy[:,1])
#    	pl.title('Vy')
#    	pl.grid()
#     
#    	pl.savefig('figure_ADCP_05_08_2015/espectros4_' + data[dc].strftime('%Y%m%d%H%M'))
#     
#     
 
 
	#processamento no dominio da frequencia particionado (sea e swell)
    hm01, tp1, dp1, hm02, tp2, dp2 = proconda.ondap(hm0,tp,dp,sn,dire1,df)

	#calculo do parametro gamma - LIOc
    gam = jonswap.gamma(tp)
    gam1 = jonswap.gamma(tp1)
    gam2 = jonswap.gamma(tp2)

	#espectro de jonswap
    s_js = jonswap.spec(hm0,tp,freq,gam)
    s_js2 = jonswap.spec(hm02,tp2,freq,gam2)

	#concatena os dados
    matonda.append([int(data[dc].strftime('%Y%m%d%H%M')),hs,h10,hmax,tmed,thmax,hm0,tp,dp,sigma1p,sigma2p,hm01,tp1,dp1,hm02,tp2,dp2,gam,gam1,gam2])

#	matondap.append([hm0_pr,tp_pr,dp_pr])

matonda = np.array(matonda)
#matondap = np.array(matondap)
#data = np.array(data)

#eta = np.array(eta).reshape(np.size(eta),1)

#cria dataframe
df = pd.DataFrame({'date':data, 'hs':matonda[:,6], 'tp':matonda[:,7], 'dp':matonda[:,8]})


df.index = df.date

del(df['date'])

df.to_csv('out/teste.csv')

evolspec = np.array(evolspec).T


pl.figure()
pl.subplot(211)
pl.plot(data,sen[:,14],'b')
pl.grid()
pl.twinx()
#pl.plot(data,matonda[:,8],'r')
pl.plot(data,coer_nnx,'r')
pl.plot(data,coer_nny,'g')
pl.plot(data,coer_nxny,'y')
#pl.ylim(0,360)
pl.subplot(212)
pl.contour(np.arange(0,len(lista)),apr[:,0],evolspec,30)
pl.xticks(range(0,len(lista),5),data[0:-1:5])
pl.ylim(0,0.5)
pl.grid()
pl.show()

'''
pl.figure()
h = pl.hist(eta,100)
pl.axis('tight')
pl.xlim(-1,1)
pl.grid()
pl.xlabel(r'$m/s$',fontsize=14)
pl.ylabel(r'$Nu\'mero\ de\ ocorre\^ncias$',fontsize=14)
pl.plot([0,0],[0,np.max(h[0])],'r--',linewidth=3)


pl.figure()
pl.plot(vz)

pl.figure()
pl.plot(sn[:,0],sn[:,1])

pl.figure()
pl.subplot(311)
pl.plot(data,matonda[:,6],label='vz')
#pl.plot(data,matondap[:,0],label='pr')
pl.legend()
pl.ylabel('Hm0 (m)')
pl.subplot(312)
pl.plot(data,matonda[:,7])
#pl.plot(data,matondap[:,1])
pl.ylabel('Tp (s)')
pl.subplot(313)
#pl.plot(data,matondap[:,2])
pl.plot(data,matonda[:,8])
pl.ylabel('Dp (graus)')

pl.figure()
pl.title('Espectros de Fase')
pl.plot(data,fase_nnx,label='nnx')
pl.plot(data,fase_nny,label='nny')
pl.plot(data,fase_nxny,label='nxny')
pl.ylabel('graus')

pl.show()

'''