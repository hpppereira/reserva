# Comparacao dos dados de onda do swell de Novembro de 2016

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from glob import glob
plt.close('all')

def create_pickle_pnboia():
    # boia - pnboia
    filelist_pnboia = glob('/home/hp/Dropbox/reserva/data/pnboia/*.csv')
    pnboia = {}
    for f in filelist_pnboia:
        print (f)
        local = f.split('/')[-1].split('.')[0]
        pnboia[local] = pd.read_csv(f, parse_dates=['Datetime'], index_col='Datetime')
        # pnboia[local] = pnboia[local].loc[dint[0]:dint[-1]]
        pnboia[local] = pnboia[local].rolling('3H').mean()
        # pnboia[local] = pnboia[local].loc[(pnboia[local].Wvht < 10) & (pnboia[local].Wvht > 0.5)]
        pnboia[local].loc[(pnboia[local].Wvht > 10) | (pnboia[local].Wvht < 0.5)] = np.nan
    pd.to_pickle(pnboia, '/home/hp/Dropbox/reserva/data/pnboia/pnboia.pkl')
    return

def create_pickle_simcosta():
    # boia - simcosta
    dateparse = lambda x: datetime.strptime(x, '%Y %m %d %H %M %S')

    dics = {'rj1': ['SIMCOSTA_RJ-1_OCEAN_2015-07-29_2016-10-13.csv', 35],
            'rj2': ['SIMCOSTA_RJ-2_OCEAN_2015-07-29_2016-12-20.csv', 35],
            'rj3': ['SIMCOSTA_RJ-3_OCEAN_2016-07-14_2021-02-12.csv', 34],
            'rj4': ['SIMCOSTA_RJ-4_OCEAN_2017-08-28_2020-12-21.csv', 34]}

    simcosta = {}
    for boia in dics.keys():
        simcosta[boia] = pd.read_csv('/home/hp/Dropbox/reserva/data/simcosta/{}'.format(dics[boia][0]),
                       skiprows=dics[boia][1], parse_dates=[['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND']],
                       date_parser=dateparse, index_col='YEAR_MONTH_DAY_HOUR_MINUTE_SECOND')
        # simcosta[boia] = simcosta[boia].loc[dint[0]:dint[-1]]
        simcosta[boia] = simcosta[boia].rolling('3H').mean()
    pd.to_pickle(simcosta, '/home/hp/Dropbox/reserva/data/simcosta/simcosta.pkl')
    return

def create_pickle_reserva():
    # rbr - reserva
    reserva = {}
    reserva['rbr'] = pd.read_csv('/home/hp/Dropbox/reserva/data/swell_reserva_201611/rbr_waveparam.csv',
                      parse_dates=['date'], index_col='date')
    reserva['rbr'] = reserva['rbr'].resample('1H').mean()
    # reserva['rbr'] = reserva['rbr'][dint[0]:dint[-1]]
    reserva['rbr'] = reserva['rbr'].rolling('3H').mean()
    pd.to_pickle(reserva, '/home/hp/Dropbox/reserva/data/swell_reserva_201611/reserva.pkl')
    return

def create_pickle_redeondas():
    dateparse = lambda x: datetime.strptime(x, '%Y %m %d %H %M %S')
    dics = {'cassino': 'cassino_cat_2016-10.txt',
            'praiadoforte': 'praiadoforte_cat_2016-10_2016-11.txt'}
    redeondas = {}
    for p in dics.keys():
        redeondas[p] = pd.read_csv('/home/hp/Dropbox/reserva/data/redeondas/{}'.format(dics[p]), sep='\t',
                         parse_dates=[['AAAA','MM','DD','hh','mm','ss']],
                         date_parser=dateparse, index_col='AAAA_MM_DD_hh_mm_ss')
        redeondas[p].index.name = 'date'
        redeondas[p] = redeondas[p].resample('1H').mean()
        redeondas[p] = redeondas[p].rolling('3H').mean()
        pd.to_pickle(redeondas, '/home/hp/Dropbox/reserva/data/redeondas/redeondas.pkl')
    return



if __name__ == "__main__":

    pratsan = {}
    pratsan['palmas'] = pd.read_csv('/home/hp/Dropbox/reserva/data/praticagem_santos/Palmas_Correntes_Ondas_2016.csv',
                                    parse_dates=True, index_col='date_hour')

    # create_pickle_pnboia()
    # create_pickle_simcosta()
    # create_pickle_reserva()
    # create_pickle_redeondas()

    pnboia = pd.read_pickle('/home/hp/Dropbox/reserva/data/pnboia/pnboia.pkl')
    simcosta = pd.read_pickle('/home/hp/Dropbox/reserva/data/simcosta/simcosta.pkl')
    reserva = pd.read_pickle('/home/hp/Dropbox/reserva/data/swell_reserva_201611/reserva.pkl')
    redeondas = pd.read_pickle('/home/hp/Dropbox/reserva/data/redeondas/redeondas.pkl')


    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(111)
    ax1.plot(pnboia['rio_grande'].Wvht, label='rio_grande')
    ax1.plot(pnboia['santos'].Wvht, label='santos')
    ax1.plot(pnboia['vitoria'].Wvht, label='vitoria')
    ax1.plot(pnboia['cabo_frio_02'].Wvht, label='cabo_frio_02')
    ax1.plot(pnboia['porto_seguro'].Wvht, label='porto_seguro')
    ax1.plot(simcosta['rj2'].Hsig, label='simcosta_rj2')
    ax1.plot(simcosta['rj3'].Hsig, label='simcosta_rj3')
    ax1.plot(reserva['rbr'].hs, label='reserva_rbr')
    ax1.plot(redeondas['cassino'].Hs, label='redeondas_cassino')
    ax1.plot(pratsan['palmas'].hs, label='pratsan_palmas')


    # nao tem dados em 2016
    # ax1.plot(pnboia['recife'].Wvht, label='recife') # nao tem dados
    # ax1.plot(pnboia['minuano'].Wvht, label='minuano') # nao tem 2016
    # ax1.plot(pnboia['cabo_frio_01'].Wvht, label='cabo_frio_01') # nao tem 2016
    # ax1.plot(pnboia['niteroi_01'].Wvht, label='niteroi_01') #dado ruim
    # ax1.plot(pnboia['niteroi_02'].Wvht, label='niteroi_02')
    # ax1.plot(pnboia['itajai'].Wvht, label='itajai') # nao tem 2016
    # ax1.plot(pnboia['fortaleza'].Wvht, label='fortaleza')
    # ax1.plot(pnboia['itaguai'].Wvht, label='itaguai')
    # ax1.plot(pnboia['itaoca'].Wvht, label='itaoca')
    # ax1.plot(simcosta['rj1'].Hsig, label='SimCosta_RJ1')
    # ax1.plot(simcosta['rj4'].Hsig, label='SimCosta_RJ4')
    # ax1.plot(redeondas['praiadoforte'].Hs, label='redeondas_praiadoforte')

    ax1.grid()
    ax1.legend(ncol=2)
    ax1.set_xlim('2016-10-25 00', '2016-11-03 23')
    plt.xticks(rotation=15)
    ax1.set_ylim(0, 9)
    plt.show()



