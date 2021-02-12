# Processamento dos dados de onda da laje da Reserva


import sys, os
import numpy as np
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'waveproc'))
import importlib
import waveproc
importlib.reload(waveproc)
plt.close('all')

if __name__ == '__main__':

    filelist = np.sort(glob('/home/hp/Dropbox/reserva/data/swell_reserva_201611/CSVs/*.csv'))

    # vetor de tempo em segundos
    dt = 0.5
    t = np.arange(0, 7200*dt, dt)

    # profundidade
    h = 200.0

    # times = []
    waves = []
    for f in filelist:

        print (f)

        rbr = pd.read_csv(f, parse_dates=['Time'], index_col='Time')

        H, T, hs, h10, hmax, tz, thmax = waveproc.ondat(t, rbr.Pressure.values, h)

        waves.append([rbr.index[0], hs, h10, hmax, tz, thmax])

    df = pd.DataFrame(np.array(waves), columns=['date', 'hs', 'h10', 'hmax', 'tz', 'thmax'])
    df.set_index('date', inplace=True)

    df.to_csv('/home/hp/Dropbox/reserva/data/swell_reserva_201611/rbr_waveparam.csv', float_format='%.2f')

    # df.index.name = 'date'


    # df_param = pd.DataFrame(wparam[:,1:], index=wparam[:,0],
    #                         columns = , 'hm0', 'tp', 'dp',
    #                         'mean_spec_period', 'mean_zup_period']).astype(float)


        # condition of numer of lines (quality control)
        # num_lines = sum(1 for line in open(filename, encoding='utf-8', errors='ignore'))

        # condicao de arquivo com todas as linhas
        # if num_lines == 1324:
            # print (filename)

            # leitura dos dados
            # df = read_axys_hne(filename)

            # processamento dos dados no dominio do tempo

            # processamento dos dados no dominio da frequencia
            # waveout = ondaf(eta=df.hv.values,
            #                 etax=df.dn.values,
            #                 etay=df.de.values,
            #                 h=h, nfft=int(len(df) / 16),
            #                 fs=1.28)

            # processamento de onda particionado
            # hm01, tp1, dp1, hm02, tp2, dp2 = ondap(waveout['hm0'], waveout['tp'],
            #                                        waveout['dp'], waveout['sn'],
            #                                        waveout['dire1'])

            # datastr = str(pd.to_datetime(filename.split('/')[-1].split('.')[0]))


            # plot_spec_dire1(df, waveout, filename)            
        # else:
            # print ('dado {} com erro'.format(filename.split('/')[-1]))

    # cria dataframe

    # salva arquivo csv
    # df_param.index.name = 'date'

