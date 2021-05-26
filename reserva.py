
import numpy as np
from matplotlib import mlab
import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')


def espec1(x, nfft, fs):
    """
    Calculo do espectro 1d
    """
    s, f = mlab.psd(x=x, NFFT=int(nfft), Fs=fs, detrend=mlab.detrend_mean,
                  window=mlab.window_hanning, noverlap=nfft/2)

    #degrees of freedom
    dof = len(x) / nfft * 2
    
    #confidence interval 95%
    ici = s * dof / 26.12
    ics = s * dof / 5.63
    
    # matriz de saida
    aa = np.array([f,s,ici,ics]).T

    return aa


# In[4]:


def espec2(x, y, nfft, fs):
    """    
    Calcula o espectro cruzado entre duas series reais
    
    Dados de entrada: x = serie real 1 (potencia de 2)
                      y = serie real 2 (potencia de 2)
                      nfft - Numero de pontos utilizado para o calculo da FFT
                      fs - frequencia de amostragem
    
    Dados de saida: [aa2] - col 0: vetor de frequencia
                            col 1: amplitude do espectro cruzado
                            col 2: co-espectro
                            col 3: quad-espectro
                            col 4: espectro de fase
                            col 5: espectro de coerencia
                            col 6: intervalo de confianca inferior do espectro cruzado
                            col 7: intervalo de confianca superior do espectro cruzado
                            col 8: intervalo de confianca da coerencia
    
    Infos:    detrend - mean
              window - hanning
              noverlap - 50%    
    """

    #cross-spectral density - welch method (complex valued)
    s, f = mlab.csd(x, y, NFFT=nfft, Fs=fs, detrend=mlab.detrend_mean, window=mlab.window_hanning, noverlap=nfft/2)

    # graus de liberdade    
    dof = len(x) / nfft * 2

    #co e quad espectro (real e imag) - verificar com parente
    co = np.real(s)
    qd = np.imag(s)
    
    #phase (angle function)
    ph = np.angle(s, deg=True)
    
    #ecoherence between x and y (0-1)
    coer = mlab.cohere(x, y, NFFT=nfft, Fs=fs, detrend=mlab.detrend_mean, window=mlab.window_hanning, noverlap=nfft/2)[0]
    # coer = coer[0][1:]
    
    #intervalo de confianca para a amplitude do espectro cruzado - 95%
    ici = s * dof /26.12
    ics = s * dof /5.63
    
    #intervalo de confianca para coerencia
    icc = np.zeros(len(s))
    icc[:] = 1 - (0.05 ** (1 / (14 / 2.0 - 1)))
    
    # matriz de saida
    aa = np.array([f, s ,co, qd, ph, coer, ici, ics, icc]).T

    return aa


df = pd.read_csv('Reserva_ADCP/ADCP_REEF_28_01_2016.wad', sep='\s+', usecols=[2,5,6,7], header=None,
    names=['pres','vx','vy','vz'])

df = df.iloc[:2048]

df['pres'] = df.pres - df.pres.mean()

df.vz.plot(kind='hist', bins=50)

plt.show()

