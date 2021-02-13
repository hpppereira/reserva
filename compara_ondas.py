# Comparacao dos dados de onda do swell de Novembro de 2016

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from glob import glob
import importlib
import pandas as pd
import folium
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker
import create_pickle_dados
importlib.reload(create_pickle_dados)


plt.close('all')

if __name__ == "__main__":

    pnboia = pd.read_pickle('/home/hp/Dropbox/reserva/data/pnboia/pnboia.pkl')
    simcosta = pd.read_pickle('/home/hp/Dropbox/reserva/data/simcosta/simcosta.pkl')
    reserva = pd.read_pickle('/home/hp/Dropbox/reserva/data/swell_reserva_201611/reserva.pkl')
    redeondas = pd.read_pickle('/home/hp/Dropbox/reserva/data/redeondas/redeondas.pkl')
    pratsan = pd.read_pickle('/home/hp/Dropbox/reserva/data/praticagem_santos/pratsan.pkl')
    pos = pd.read_pickle('/home/hp/Dropbox/reserva/data/posicoes.pkl')

    # plota series temporais
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

    # plota mapa com os pontos
    fig = plt.figure(figsize=(8,6))
    map_proj = ccrs.Mercator()
    ax = fig.add_subplot(1,1,1, projection=map_proj)
    ax.set_title('Pontos de medições')
    ax.coastlines()
    ax.set_extent([-53, -25, -35, -2.4], crs=ccrs.PlateCarree())
    ax.scatter(x=pos.lon.values, y=pos.lat.values, color="red", s=50,
               alpha=1, transform=ccrs.PlateCarree())
    ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                 linewidth=2, color='gray', alpha=0.5, linestyle='--')

    plt.show()




