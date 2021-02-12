

import pandas as pd

df1 = pd.read_csv('/home/hp/Dropbox/reserva/data/pnboia/pnboia_santos.csv',
				 parse_dates=['Datetime'], index_col='Datetime')

df = df1['2016-11']