# Separa arquivos horarios da laje
# do sheraton

import pandas as pd

df = pd.read_csv('/home/hp/Dropbox/reserva/data/swell_reserva_201611/Swell_reserva_201611_data.txt',
    parse_dates=['Time'], index_col='Time')

timestr = df.resample('30Min').mean().index.strftime('%Y-%m-%d %H:%M')
timestrcsv = df.resample('30Min').mean().index.strftime('%Y%m%d%H%M00')

for i in range(len(timestr)):
	print (timestr[i])
	df1 = df[timestr[i]]
	df1.to_csv('/home/hp/Dropbox/reserva/data/swell_reserva_201611/CSVs/reserva_{}.csv'.format(timestrcsv[i]))

