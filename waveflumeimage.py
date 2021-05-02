'''

install anaconda
conda install -c https://conda.binstar.org/menpo opencv
'''

import os
import numpy as np
import cv2
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import pylab as pl
from pylab import *
import pandas as pd
from PIL import Image
import matplotlib.image as mpimg
from skimage import color



#pl.close('all')

#captura imagem com ffmpeg

pathname = os.environ['HOME'] + '/Dropbox/reserva/imagens/'

def getframes(pathname, moviefile, framei, framef, freq, fileout):

    frames = pd.date_range(framei, framef, freq=freq).format(formatter=lambda x: x.strftime('%H:%M:%S.%f'))
    
    cont = 0
    for frame in frames:
        cont += 1
        os.system('cd ' + pathname  + '\n' + 
                  'ffmpeg -i ' + moviefile + ' -ss ' + frame + ' -f image2 -vframes 1 ' + fileout + str(cont) + '.png')


def get_tank_grid_scale():
    scale_height = plt.ginput(n=2)
    symax, symin = scale_height[0][1], scale_height[1][1]
    pixel_ref = int( round(symax-symin) )



########################################################################

#get frame from video

#getframes(pathname  = pathname,
#          moviefile = 'onda.wmv',
#          framei    = '00:00:01.000',
#          framef    = '00:00:05.000',
#          freq      = '30ms',
#          fileout   = 'img')


#limites para detectar a derivada que representa a onda e o fundo (valores positivos)
wlim =  0.03
blim = -0.03

#janela movel
wsw = 10
wsb = 2



#fname = 'img28.png'

figlist = np.sort(os.listdir(pathname))[:-1]


for fname in figlist[0:]:

    #limite para mapear o fundo e a onda


    #load the image with cv2

    #img = cv2.imread('../imagens/img1.png',0)
    #img = plt.imread(pathname + fname,0)
    #img = Image.open(pathname + fname).convert("L")
    img = color.rgb2gray(mpimg.imread(pathname + fname));

    #color convert
    #img = matplotlib.colors.rgb_to_hsv(img)

    #subset
    img = img[504:700, 724:1110]


    #rolling mean
    img = np.array(pd.rolling_mean(img.T, 3))
    img = img.T

    #retira os nan criado pela media movel
    img = img[:,~np.isnan(img[0,:])]

    ###########################################################################
    ###########################################################################

    # #tenta criar perfil de onda

    pwav = []
    pbot = []
    serie = []

    for j in range(img.shape[1]):

        #matriz de cada derivada menos a media das deriadas totais
        w = np.diff(img[:,j] - np.nanmean(img))
        w = pd.rolling_mean(w, wsw)
        
        b = np.diff(img[:,j] - np.nanmean(img))
        #b = pd.rolling_mean(b, wsb)

        #b = np.flipud(a) #bottom

        #normalize vector
        #a = a / a.sum()
        #b = b / b.sum()
        
        # pl.figure()
        # pl.plot(a)
        # pl.savefig('out/der' + str(j) + '.png')
        # pl.close('all')

        #perfil da onda (pwav) e fundo (pbot)

        #acha o fundo
        #acha valores menores que zero (fundo)
        auxwav = pl.find(w > wlim)[1]
        pwav.append(auxwav)

        auxbot = pl.find(b < blim)[-1]
        pbot.append(auxbot)

        #pbot.append( len(b) - pl.find(b < -blim)[0] ) #faz a contagem do inverso

#        pwav.append(pl.find(a > wlim)[0])
                        
#        pbot.append(pl.find(a == a.min())[-1])


    #pwav = pd.rolling_mean(np.array(pwav), wind)
    #pbot = pd.rolling_mean(np.array(pbot), wind)

    fig = plt.figure( figsize=(10,8) )
    ax  = fig.add_subplot(111)
    implot = ax.imshow(img, aspect='equal', interpolation='bicubic', cmap=plt.get_cmap('gray'))
    ax.plot(pwav, color='r', lw = 1.5)
    ax.plot(pbot, color='r', lw = 1.5)
    fig.savefig('out/imagens/' + fname)

    #pl.close('all')






plt.show()








