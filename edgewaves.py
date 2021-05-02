'''
Calcula a edge wave teorica

artigo: 
infragravity waves in the surf zone
'''


import numpy as np
import pylab as pl

pl.close('all')

#distance to shore
x = np.arange(0,1000,0.1)
t = x

#shoreline amplitude of the nth mode
a = 1

#edge wave period (seconds)
T = 50
g = 9.81
n = 1 

#comprimento da edge wave
L = (g/2*3.14) * T**2 * sin(2*n+1)* 0.07

#order Laguere polynomial ??
Ln0 = np.ones(len(x))
Ln1 = -x + 1
Ln2 = (1.0 / 2) * ( (x**2) - (4 * x) + 2)
Ln3 = (1.0 / 6) * ( (-x**3) + (9 * x**2) - (18 * x) + 6)

#gravitational accel.
g = 9.8

#numero de onda (k)
k = 2 * np.pi / L

#radial frequency
s = 2 * np.pi / T


#distace normalized
xn = s**2 * x / g


#eq. 3 - offshore behavior
aux0 = np.exp(-k*x) * Ln0 * (2 * k * x)
aux1 = np.exp(-k*x) * Ln1 * (2 * k * x)
aux2 = np.exp(-k*x) * Ln2 * (2 * k * x)
aux3 = np.exp(-k*x) * Ln3 * (2 * k * x)


#eq. 2
ew0 = (a * g / s) * np.cos(k*x - s*t) * aux0
ew1 = (a * g / s) * np.cos(k*x - s*t) * aux1
ew2 = (a * g / s) * np.cos(k*x - s*t) * aux2
ew3 = (a * g / s) * np.cos(k*x - s*t) * aux3


#pl.figure()
pl.plot(x,ew0)
pl.plot(x,ew1)
pl.plot(x,ew2)
pl.plot(x,ew3)


pl.show()