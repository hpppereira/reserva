# Cria pickle com pontos de medicoes e plota no mapa

import pandas as pd
import folium
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker

plt.close('all')

# def plot_map(lon, lat, vv, u10, v10, tmes, title, time):
#     """
#     """
#     fig = plt.figure(figsize=(8,6))
#     map_proj = ccrs.Mercator()
#     ax = fig.add_subplot(1,1,1, projection=map_proj)
#     ax.set_title(title)
#     ax.coastlines()
#     ax.set_extent([lon.max(), lon.min(),
#                    lat.max(), lat.min()],
#                    crs=ccrs.PlateCarree())

#     cont = ax.contourf(lon, lat, vv[time,:,:],
#            # np.arange(18,42,1), 
#               transform=ccrs.PlateCarree())

#     # colorbar
#     divider = make_axes_locatable(ax)
#     ax_cb = divider.new_horizontal(size="5%", pad=0.1, axes_class=plt.Axes)
#     fig.add_axes(ax_cb)
#     cbar = plt.colorbar(cont, cax=ax_cb)
#     cbar.set_label('hPa', rotation=0)
    
#     ax.scatter(
#         x=tmes['posicoes'].lon,
#         y=tmes['posicoes'].lat,
#         color="red",
#         s=10,
#         alpha=1,
#         transform=ccrs.PlateCarree()
#         )

#     ax.quiver(lon[::5], lat[::5], u10[time,::5,::5], v10[time,::5,::5],
#         transform=ccrs.PlateCarree())

#     ax.set_xticks(lon[::10], crs=ccrs.PlateCarree())
#     ax.set_yticks(lat[::10], crs=ccrs.PlateCarree())
#     lon_formatter = LongitudeFormatter(number_format='.1f',
#                                        degree_symbol='',
#                                        dateline_direction_label=True)
#     lat_formatter = LatitudeFormatter(number_format='.1f',
#                                       degree_symbol='')
#     ax.xaxis.set_major_formatter(lon_formatter)
#     ax.yaxis.set_major_formatter(lat_formatter)
#     return fig

if __name__ == "__main__":

    pos = pd.read_pickle('/home/hp/Dropbox/reserva/data/posicoes.pkl')

    # state_borders = cfeat.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lakes',
    #                                           scale='50m', facecolor='none')

    # fig = plt.figure(figsize=(8,6))
    # map_proj = ccrs.Mercator()
    # ax = fig.add_subplot(1,1,1, projection=map_proj)
    # ax.set_title('Pontos de medições')
    # ax.coastlines()
    # ax.set_extent([-53, -25, -35, -2.4], crs=ccrs.PlateCarree())

    # ax.set_extent([lon.max(), lon.min(),
    #                lat.max(), lat.min()],
    #                crs=ccrs.PlateCarree())

    # cont = ax.contourf(lon, lat, vv[time,:,:],
    #        # np.arange(18,42,1), 
    #           transform=ccrs.PlateCarree())

    # colorbar
    # divider = make_axes_locatable(ax)
    # ax_cb = divider.new_horizontal(size="5%", pad=0.1, axes_class=plt.Axes)
    # fig.add_axes(ax_cb)
    # cbar = plt.colorbar(cont, cax=ax_cb)
    # cbar.set_label('hPa', rotation=0)
    
    ax.scatter(
        x=pos.lon.values,
        y=pos.lat.values,
        color="red",
        s=50,
        alpha=1,
        transform=ccrs.PlateCarree()
        )

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=2, color='gray', alpha=0.5, linestyle='--')

    # gl.xlabels_top = False
    # gl.ylabels_left = False
    # gl.xlines = False
    # gl.xlocator = mticker.FixedLocator([-180, -45, 0, 45, 180])
    # gl.xformatter = LONGITUDE_FORMATTER
    # gl.yformatter = LATITUDE_FORMATTER
    # gl.xlabel_style = {'size': 15, 'color': 'gray'}
    # gl.xlabel_style = {'color': 'red', 'weight': 'bold'}

    # ax.quiver(lon[::5], lat[::5], u10[time,::5,::5], v10[time,::5,::5],
    #     transform=ccrs.PlateCarree())

    # ax.set_xticks(lon[::10], crs=ccrs.PlateCarree())
    # ax.set_yticks(lat[::10], crs=ccrs.PlateCarree())

    # lon_formatter = LongitudeFormatter(number_format='.1f',
    #                                    degree_symbol='',
    #                                    dateline_direction_label=True)
    # lat_formatter = LatitudeFormatter(number_format='.1f',
    #                                   degree_symbol='')
    # ax.xaxis.set_major_formatter(lon_formatter)
    # ax.yaxis.set_major_formatter(lat_formatter)

    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())

    # # ax.add_feature(cfeat.LAND)
    # # ax.add_feature(cfeat.OCEAN)
    # ax.add_feature(cfeat.COASTLINE)
    # # ax.add_feature(cfeat.BORDERS, linestyle=':')
    # # ax.add_feature(cfeat.RIVERS)
    # ax.add_feature(state_borders, linewidth=0.2, edgecolor='black')
    # ax.gridlines()
    # ax.scatter(pos.lon.values, pos.lat.values, transform=ccrs.PlateCarree(), marker='.', s=100, c='r')

    ax.set_extent([-53, -25, -35, -2.4])

    plt.show()

    # # plota campo de pressao e vento
    # time = 0
    # title = '{}\nPressão Atmosférica no Nível do Mar e Velocidade do Vento a 100 m'.format(
    # pd.to_datetime(d['ma_dt302_v'].index[0]).strftime('%Y-%m-%d %Hh'))

    # fig = plot_map(lon=ds.longitude.values, lat=ds.latitude.values, vv=ds['msl'].values,
    #                u10=ds['u100'].values, v10=ds['v100'].values, tmes=tmes, title=title, time=time)

    # fig.savefig(pathname2 + 'A1F_cf_040_msl_wind.png', bbox_inches='tight')
    # plt.close('all')


    # plota mapas iterativos
    # brasil = folium.Map(location=[-23, -41], zoom_start=5)
    # for p in pos.index:
    #     folium.Marker(location=[pos.loc[p].lat, pos.loc[p].lon], popup='{}\n{}m'.format(p, pos.loc[p].depth)).add_to(brasil)
    # brasil.save('pontos_medicao.html')

