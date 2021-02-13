# processamento dos dados do waverys

import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from mpl_toolkits.axes_grid1 import make_axes_locatable
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter


plt.close('all')

def imprime_variaveis(ds):
    """
    imprime nos das variaveis
    """
    for v in list(ds.data_vars):
        print (v + ' -- ' + ds[v].long_name)
    return

if __name__ == "__main__":

    wav = xr.open_dataset('/home/hp/Dropbox/reserva/data/waverys/global-reanalysis-wav-001-032_1613235011924.nc')
    imprime_variaveis(wav)

    lat = wav.latitude.data
    lon = wav.longitude.data
    vv = wav['VHM0_WW'].values
    time = 30

    fig = plt.figure(figsize=(8,6))
    map_proj = ccrs.Mercator()
    ax = fig.add_subplot(1,1,1, projection=map_proj)
    ax.set_title('WAVERYS')
    ax.coastlines()
    ax.set_extent([lon.max(), lon.min(),
                   lat.max(), lat.min()],
                   crs=ccrs.PlateCarree())

    cont = ax.contourf(lon, lat, vv[time,:,:],
           # np.arange(18,42,1), 
              transform=ccrs.PlateCarree())

    # colorbar
    divider = make_axes_locatable(ax)
    ax_cb = divider.new_horizontal(size="5%", pad=0.1, axes_class=plt.Axes)
    fig.add_axes(ax_cb)
    cbar = plt.colorbar(cont, cax=ax_cb)
    cbar.set_label('Hs', rotation=0)
    
    # ax.scatter(
    #     x=tmes['posicoes'].lon,
    #     y=tmes['posicoes'].lat,
    #     color="red",
    #     s=10,
    #     alpha=1,
    #     transform=ccrs.PlateCarree()
    #     )

    # ax.quiver(lon[::5], lat[::5], u10[time,::5,::5], v10[time,::5,::5],
    #     transform=ccrs.PlateCarree())

    ax.set_xticks(lon[::25], crs=ccrs.PlateCarree())
    ax.set_yticks(lat[::25], crs=ccrs.PlateCarree())
    lon_formatter = LongitudeFormatter(number_format='.1f',
                                       degree_symbol='',
                                       dateline_direction_label=True)
    lat_formatter = LatitudeFormatter(number_format='.1f',
                                      degree_symbol='')
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)

    plt.show()






    stop


    # ds_era5 = xr.open_dataset(pathname3 + 'ERA5_param_fortaleza.nc')
    # boia = pd.read_csv(pathname2 + 'pnboia_fortaleza.csv', parse_dates=True, index_col='Datetime')


    # # seleciona dados para salinopolis e cria dataframe
    # wave = ds_wave.sel(latitude=p['for'][0], longitude=p['for'][1], method='nearest').to_dataframe()
    # era5 = ds_era5.sel(latitude=p['for'][0], longitude=p['for'][1], method='nearest').to_dataframe()

    # boia = boia.rolling(window=3, center=True).mean()
    # boia = boia.resample('3H').mean()

    # # pega o mesmo periodo nos dados e no modelo
    # boia = boia['2017-01-01 00:00:00':'2017-12-31 21:00:00']
    # wave = wave['2017-01-01 00:00:00':'2017-12-31 21:00:00']

    # boia.to_csv('boia.csv', float_format='%.2f')
    # wave.to_csv('wave.csv', float_format='%.2f')

    # stop

    # print ('\n')
    # print (list(wav.columns))
    # print ('\n')
    # print (list(era.columns))

    # # plotagem dos dados do pnboia e do era5 de fortaleza
    # fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12,10), sharex=True)
    # # ax1 = fig.add_subplot(311)
    # axes[0].set_title('Fortaleza/CE')
    # boia.Wvht.plot(ax=axes[0], ylim=(0,4), label='Boia')
    # wav.VHM0.plot(ax=axes[0], label='WAVERYS')
    # wav.VHM0_SW1.plot(ax=axes[0], label='WAVERYS_swell')
    # wav.VHM0_WW.plot(ax=axes[0], label='WAVERYS_sea')
    # # era.swh.plot(ax=axes[0], label='ERA5')
    # axes[0].set_ylabel('Hs (m)')
    # axes[0].legend(ncol=2)
    # # axes[0].grid('on', which='major')
    # # axes[0].grid('off', which='major', axis='xy' )
    # axes[0].grid()
    # # boia.Dpd.plot(ax=axes[1], ylim=(4,22), label='tp_boia')
    # wav.VTPK.plot(ax=axes[1], label='total')
    # # wav.VTM01_SW1.plot(ax=axes[1], label='swell')
    # wav.VSDX.plot(ax=axes[1], label='stokes_U')
    # wav.VSDY.plot(ax=axes[1], label='stokes_V')
    # axes[1].set_ylabel('Tp (s)')
    # axes[1].grid()
    # axes[1].legend()
    # # ax3 = fig.add_subplot(313)
    # boia.Mwd.plot(ax=axes[2], ylim=(0, 150))
    # wav.VMDR.plot(ax=axes[2])
    # axes[2].set_ylabel('Dp º')
    # axes[2].grid()
    # axes[2].set_xlim(wav.index[0], wav.index[-1])

    # plt.show()
