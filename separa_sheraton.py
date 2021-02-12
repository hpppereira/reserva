# Separa arquivos horarios da laje
# do sheraton

import pandas as pd

df = pd.read_csv('/home/hp/Dropbox/reserva/data/Laje_Sheraton/Swell_reserva_201611/Swell_reserva_201611_data.txt',
    parse_dates=['Time'], index_col='Time')

timestr = df.resample('H').mean().index.strftime('%Y-%m-%d %H')
timestrcsv = df.resample('H').mean().index.strftime('%Y%m%d%H')

for i in range(len(timestr)):
    df1 = df[timestr[i]]
    df1.to_csv('/home/hp/Documents/sheraton/sheraton_{}.csv'.format(timestrcsv[i]))

