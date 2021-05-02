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
wlim = abs(0.05)
blim = abs(0.05)

#janela movel
wind = 5 


#fname = 'img28.png'

figlist = np.sort(os.listdir(pathname))[:-1]


for fname in figlist[0:1]:

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

        #cria primeiro ponto como referencia

        if j == 0:

            #matriz de cada derivada menos a media das deriadas totais
            a = np.diff(img[:,j] - np.nanmean(img))

            #normalze vector
            #a = a / a.sum()
            
            #perfil da onda (pwav) e fundo (pbot)
            pwav.append(int(pl.find(a == np.nanmax(a))[0]))
            pbot.append(int(pl.find(a == np.nanmin(a))[0]))

        else:

            #matriz de cada derivada menos a media das deriadas totais
            a = np.diff(img[:,j] - np.nanmean(img))
            b = np.flipud(a) #bottom

            #normalze vector
            #a = a / a.sum()
            #b = b / b.sum()
            
            #perfil da onda (pwav) e fundo (pbot)
            pbot.append(len(b) - pl.find(b < -blim)[0]) #faz a contagem do inverso
            pwav.append(pl.find(a > wlim)[0])
            
            
            #pbot.append(pl.find(a == a.min())[-1])


    pwav = pd.rolling_mean(np.array(pwav), wind)
    pbot = pd.rolling_mean(np.array(pbot), wind)

    fig = plt.figure( figsize=(10,8) )
    ax  = fig.add_subplot(111)
    implot = ax.imshow(img, aspect='equal', interpolation='bicubic', cmap=plt.get_cmap('gray'))
    ax.plot(pwav, color='r', lw = 1.5)
    ax.plot(pbot, color='r', lw = 1.5)

    fig.savefig('out/imagens/' + fname)

#    plt.close('all')


















#dx, dy = np.gradient(img)


#converting to gray scale
#gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


# '''
# imgi = img1
# imgf = img2

# # remove noise
# img_1 = cv2.GaussianBlur(imgi,(5,5),0)
# img_2 = cv2.GaussianBlur(imgf,(5,5),0)

# # convolute with proper kernels
# lap1 = cv2.Laplacian(img_1,cv2.CV_64F)
# lap2 = cv2.Laplacian(img_2,cv2.CV_64F)

# sobelx1 = cv2.Sobel(img_1,cv2.CV_64F,1,0,ksize=5)  # x
# sobely1 = cv2.Sobel(img_1,cv2.CV_64F,0,1,ksize=29)  # y

# sobelx2 = cv2.Sobel(img_2,cv2.CV_64F,1,0,ksize=5)  # x
# sobely2 = cv2.Sobel(img_2,cv2.CV_64F,0,1,ksize=29)  # y

# img55 = sobely2 - sobely1 #lap2 - lap1 #


# # Passando para valores entre 0 e 1:
# img1 = (img55 + abs(img55.min()))
# img11 = img1/img1.max()           

# #print img11.min(), img11.max()

# # Mudando de formato para uint8
# imgdif = (img11* 255).round().astype(np.uint8)

# #------------------
# (L,C)=shape(imgdif)

# img=imgdif
# img22=imgdif

# fator = 3

# for m in range(0,C):
#     std1=std(img[:,m])
#     med=mean(img[:,m])
#     istdU= find( img[:,m] > (med + fator *std1))
#     istdD= find( img[:,m] < (med - fator *std1))
    
#     img22[istdU,m]=0
#     img22[istdD,m]=0
# #plt.plot(img[:,10])

# '''






    #a1 = np.diff(a)
    #a2 = pd.rolling_mean(a1,80)

    #p.append( pl.find( np.diff(img[:,m]) == np.diff(img[:,m]).max() ) )
    #p1.append( pl.find( a1 == a1.max() ) )
    #p2.append( pl.find( a2 == np.nanmax(a2) ) )

    #p.append( pl.find(np.diff(img55[450:550,m]) == np.diff(img55[450:550,m]).max()  )   )
#     #p1.append( pl.find(np.diff(np.diff(img55[450:550,m])) == np.diff(np.diff(img55[450:550,m])).max()  )   )

# p = np.array(p) + z1
# p1 = np.array(p1) + z1
# p2 = np.array(p2) + z1

# #media movel do perfil de onda
# mm = 50
# p = pd.rolling_mean(p,mm)
# p1 = pd.rolling_mean(p1,mm)
# p2 = pd.rolling_mean(p2,mm)



# fig = plt.figure( figsize=(10,8) )

# ax  = fig.add_subplot(111)

# implot = ax.imshow(img1, aspect='equal', interpolation='bicubic')

# #rectangle = plt.ginput(n=2, timeout=60)
# rectangle = [(573.62499999999989, 680.92857142857144),
#              (1177.9107142857142, 462.35714285714289)]


# xmin, ymax = rectangle[0]
# xmax, ymin = rectangle[1]

# ax = implot.get_axes()

# ax.set_ybound([ ymin, ymax ])
# ax.set_xbound([ xmin, xmax ])



# # pl.plot(p,'r')
# # pl.plot(p1,'y')
# # pl.plot(p2,'g')


# # #pm = np.mean([p,p1,p2])


# # #pl.colorbar()


# # pl.show()


# #plt.imshow(imgdif)
# #plt.show()


# #plt.imshow(img1),#cmap = 'gray')

# plt.show()

