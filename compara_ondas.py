# Comparacao dos dados de onda do swell de Novembro de 2016

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from glob import glob
plt.close('all')

dint = ['2016-10-10', '2016-12-10']

# rbr - reserva
rbr = pd.read_csv('/home/hp/Dropbox/reserva/data/swell_reserva_201611/rbr_waveparam.csv',
                  parse_dates=['date'], index_col='date')
rbr = rbr.resample('1H').mean()
rbr = rbr[dint[0]:dint[-1]]

# pnboia
filelist_pnboia = glob('/home/hp/Dropbox/reserva/data/pnboia/*.csv')
pnboia = {}
for f in filelist_pnboia:
    local = f.split('/')[-1].split('.')[0]
    pnboia[local] = pd.read_csv(f, parse_dates=['Datetime'], index_col='Datetime')
    pnboia[local] = pnboia[local].loc[dint[0]:dint[-1]]
    pnboia[local] = pnboia[local].rolling('3H').mean()


# simcosta
dateparse = lambda x: datetime.strptime(x, '%Y %m %d %H %M %S')

rj2 = pd.read_csv('/home/hp/Dropbox/reserva/data/simcosta/SIMCOSTA_RJ-2_OCEAN_2015-07-29_2016-12-20.csv',
                   skiprows=35, parse_dates=[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND']],
                   date_parser=dateparse, index_col='YEAR_MONTH_DAY_HOUR_MINUTE_SECOND')
rj3 = pd.read_csv('/home/hp/Dropbox/reserva/data/simcosta/SIMCOSTA_RJ-3_OCEAN_2016-07-14_2021-02-12.csv',
                   skiprows=34, parse_dates=[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND']],
                   date_parser=dateparse, index_col='YEAR_MONTH_DAY_HOUR_MINUTE_SECOND')
rj2 = rj2.loc[dint[0]:dint[-1]]
rj3 = rj3.loc[dint[0]:dint[-1]]


rbr = rbr.rolling('3H').mean()
rj2 = rj2.rolling('3H').mean()
rj3 = rj3.rolling('3H').mean()


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(pnboia['santos'].Wvht, label='santos')
# ax1.plot(pnboia['itajai'].Wvht, label='itajai')
ax1.plot(pnboia['porto_seguro'].Wvht, label='porto_seguro')
ax1.plot(pnboia['rio_grande'].Wvht, label='rio_grande')
ax1.plot(pnboia['fortaleza'].Wvht, label='fortaleza')
ax1.plot(pnboia['cabo_frio'].Wvht, label='cabo_frio')
ax1.plot(rbr.hs, label='Reserva')
ax1.plot(rj2.Hsig, label='SimCosta_RJ2')
ax1.plot(rj3.Hsig, label='SimCosta_RJ2')
ax1.legend()
ax1.set_ylim(0,9)
plt.show()