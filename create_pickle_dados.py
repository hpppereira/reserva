# cria pickle das variaveis

from glob import glob
import pandas as pd
import numpy as np
from datetime import datetime

def create_pickle_pnboia():
    # boia - pnboia
    filelist_pnboia = glob('/home/hp/Dropbox/reserva/data/pnboia/*.csv')
    pnboia = {}
    for f in filelist_pnboia:
        # print (f)
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

def create_pickle_pratsan():
    pratsan = {}
    pratsan['palmas'] = pd.read_csv('/home/hp/Dropbox/reserva/data/praticagem_santos/Palmas_Correntes_Ondas_2016.csv',
                                    parse_dates=True, index_col='date_hour')
    pratsan['palmas'].index.name = 'date'
    pratsan['palmas'] = pratsan['palmas'].resample('1H').mean()
    pratsan['palmas'] = pratsan['palmas'].rolling('3H').mean()
    pd.to_pickle(pratsan, '/home/hp/Dropbox/reserva/data/praticagem_santos/pratsan.pkl')
    return

def create_pickle_locations():
    """
    lista de posicoes com os dados
    """
    # lat, lon, depth
    pos = {}
    pos['rio_grande'] = [-31.566, -49.966, 200]
    pos['santos'] = [-25.283, -44.933, 200]
    pos['vitoria'] = [-20.278, -39.727, 200]
    pos['cabo_frio'] = [-22.995, -42.187, 60]
    pos['porto_seguro'] = [-18.151, -37.944, 200]
    pos['simcosta_rj2'] = [-22.931944, -43.147778, 20]
    pos['simcosta_rj3'] = [-22.983056, -43.174444, 20]
    pos['reserva_rbr'] = [-23.017752, -43.366500, 12.0]
    pos['redeondas_cassino'] = [-32.3397222, -51.8980556, 10.0]
    pos['pratsan_palmas'] = [-24.008593, -46.328842, 10]
    pos = pd.DataFrame(pos).T
    pos.columns = ['lat','lon', 'depth']
    pd.to_pickle(pos, '/home/hp/Dropbox/reserva/data/posicoes.pkl')    
    return

create_pickle_pnboia()
create_pickle_simcosta()
create_pickle_reserva()
create_pickle_redeondas()
create_pickle_pratsan()
create_pickle_locations()