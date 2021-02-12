# Processamento de dados de onda da laje do sheraton

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from glob import glob
plt.close('all')

if __name__ == "__main__":

    filelist = np.sort(glob('/home/hp/Documents/sheraton/csvs/sheraton*.csv'))

    for f in filelist:
        df = pd.read_csv(f, parse_dates=['Time'], index_col='Time')

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.plot(df.Pressure)
        fig.savefig('/home/hp/Documents/sheraton/figs/{}.png'.format(f.split('/')[-1][:-4]))
        plt.close('all')
