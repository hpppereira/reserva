'''
Processamento dos dados de mare
de Ilha Fiscal da MB

Taxa de amostragem: 5 min
Periodo ini: 01/01/2015
Periodo fim: 23/09/2015
'''

import pandas as pd
import espec
import matplotlib.pylab as pl
import numpy as np

pl.close('all')

#pathname = os.environ['HOME'] + '/Dropbox/nemes/dados/Maregrafo_MB/'
pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/Maregrafo_MB/'

#carrega dados previstos no sisbahia
dfp = pd.read_table(pathname + 'mare_prev.txt', sep='\t')

#carrega dados marinha
df = pd.read_table(pathname + '50140004130101201523092015ALT.txt', sep=';', skiprows=11, names=['date','mare','nan'])

#remove a utlima coluna que foi criada com nan
df = df.drop(df.columns[2], axis=1)

#coloca data em datetime
df.index = pd.to_datetime(df.date, format='%d/%m/%Y %H:%M')
dfp.index = df.index

#mare mateorologica
dfp.mm = df.mare - dfp.prev
mmm =  df.mare - dfp.prev

#dfp.index = pd.to_datetime(dfp.date, format='%d/%m/%Y %H:%M')

fs = 1.0 / (5.0 / 60 / 24)
nfft = len(df) / 2

#calculo do espectro
aa = espec.espec1(df.mare,nfft,fs)

#espectro mare meteo
aamm = espec.espec1(dfp.mm,nfft,fs)
aap = espec.espec1(dfp.prev,nfft,fs)

#achar a onda de mare meteo
dfp.Mareonda = pd.rolling_mean(dfp.mm,1080)
onda = dfp.Mareonda-np.mean(dfp.Mareonda)

pl.figure()
pl.plot(df.index,df.mare)

pl.figure()
pl.semilogx(aa[:,0],aa[:,1],'b')
pl.semilogx(aamm[:,0],aamm[:,1],'r')
pl.semilogx(aap[:,0],aap[:,1],'k')
pl.grid()
pl.legend(['nivel_medido','prev'])
pl.xlabel('Freq. (cpd)')
pl.ylabel('m2/cpd')

pl.figure()
pl.subplot(211)
pl.plot(df.index,df.mare - np.mean(df.mare),'b',df.index,dfp.prev - np.mean(dfp.prev),'r')
pl.legend(['Mare_Medido','Mare_Harminicos'])
pl.subplot(212)
pl.plot(dfp.index,dfp.mm-np.mean(dfp.mm))
pl.plot([dfp.index[0],dfp.index[-1]],[0,0],'r--')
#pl.plot(dfp.index,onda,'k')
pl.legend(['Nivel_Nao_astronomico'])









pl.show()