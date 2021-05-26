'''
Plotagem da evolucao do espectro
'''

import os
import numpy as np
import espec
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import proconda
import espec

plt.close('all')

pathname = os.environ['HOME'] + '/Dropbox/projects/reserva/dados/ADCP_Reef_Reserva/'
#pathname = 'C:/Users/douglas.MENTAWAII/Dropbox/nemes/dados/ADCP_Reef_Reserva/'

#divisao da transformada de fourier
dft = 8 #2=4gl ; 4=8gl ...


lista = np.sort(os.listdir(pathname))

#escolhe o dia (fazer: entrar com string de data)
days = lista[:]

for day in days[:]:

	if day <> '20151120':

		print day
	 
		listarq = np.sort(os.listdir(pathname + day))
	
		#selecionando e carregando o .wad (com todos os burst)
		for i in range(len(listarq)):
		    if listarq[i].endswith(day[0:4] + '.wad'): #nao seleciona os arquivos .wad de cada burst
		        print listarq[i]
		        wad = pd.read_table(pathname + day + '/' + listarq[i], sep='\s*', header=None, index_col=False,
		            names=['bur','coun','pres','spare','analog','vxe','vyn','vzu','amp1','amp2','amp3','ampna'])


		#cria matriz de zeros da dimensao que tem que ter
		aux = np.zeros((wad.coun[wad.bur == 1].iloc[-1], wad.bur.iloc[-1]))
		#aux = []

		#contador para remover burst que nao estao completos

		aux_pres = []
		aux_vxe = []
		aux_vyn = []
		aux_vzu = []

		cont = 0
		#varia as colunas
		for i in range(wad.bur.iloc[-1]):
			cont += 1

			#.values transforma dataframe em array (importante para o append)
			if wad.pres[wad.bur == cont].min() > 0.5: #pega pressao maior que 0.5 (adcp dentro a)

				aux_pres.append(wad.pres[wad.bur == cont].values)
				aux_vxe.append(wad.vxe[wad.bur == cont].values)
				aux_vyn.append(wad.vyn[wad.bur == cont].values)
				aux_vzu.append(wad.vzu[wad.bur == cont].values)

		#python list of np arrays to array
		wad_pres = np.vstack(aux_pres).T
		wad_vxe = np.vstack(aux_vxe).T
		wad_vyn = np.vstack(aux_vyn).T
		wad_vzu = np.vstack(aux_vzu).T

		#coloca todas as variaveis dentro e um dicionario
		di = {}
		di = {'pres': wad_pres,
			  'vxe': wad_vxe,
			  'vyn': wad_vyn,
			  'vzu': wad_vzu
		}

		aux_hm0 = []
		aux_tp = []
		aux_dp = []
#		aux_esp = []
		aux_esp_pr = []
		aux_esp_vx = []
		aux_esp_vy = []
		aux_esp_vz = []
		
		#processa cada serie
		for i in range(di['pres'].shape[1]):

			#parameters for spectral calculation
			depth = di['pres'][:,i].mean() + 0.9
			nfft = len(di['pres']) / dft
			fs = 2 #sample freq
				
			#calcula parametros de ondas
			hm0, tp, dp, sigma1, sigma2, sigma1p, sigma2p, freq, df, k, sn, snx,sny, snn, snnx, snny, snxny, snxnx, snyny, a1, b1, a2, b2, dire1, dire2 = proconda.ondaf(
				di['vzu'][:,i],di['vxe'][:,i],di['vyn'][:,i],depth,nfft,fs)

			#concatena os parametros de onda
			aux_hm0.append(hm0)
			aux_tp.append(tp)
			aux_dp.append(dp)

			#concatena os espectros
			aux_esp_pr.append(espec.espec1(di['pres'][:,i], nfft, fs)[:,1])
			aux_esp_vx.append(espec.espec1(di['vxe'][:,i],  nfft, fs)[:,1])
			aux_esp_vy.append(espec.espec1(di['vyn'][:,i],  nfft, fs)[:,1])
			aux_esp_vz.append(espec.espec1(di['vzu'][:,i],  nfft, fs)[:,1])

			#cria array com os parametros e espectros concatenados
			hm0 = np.array(aux_hm0)
			tp = np.array(aux_tp)
			dp = np.array(aux_dp)
			esp_pr = np.array(aux_esp_pr).T
			esp_vx = np.array(aux_esp_vx).T
			esp_vy = np.array(aux_esp_vy).T
			esp_vz = np.array(aux_esp_vz).T
			
			##################################################


			#ax4.set_xticklabels(ax4.get_xticks(), visible=True, rotation=5)
			#ax4.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))

			#fig.savefig('fig/evolspec_201302_a.png', bbox_inches='tight')

			#velocidade para amplitude
			#aux = np.ones
			#esp = esp / (2*np.pi*freq)**2

			#o None cria dimensao de uma coluna
			#w2 = 2 * np.pi * freq[:,None] **2
			
			fig = plt.figure()
			ax1 = fig.add_subplot(221)
			ax1.set_title(day)
			ax1.plot(freq,esp_pr[:,i])
			# ax1.plot(di['pres'][:,i])
			ax1.legend(['pr'])
			#ax1.set_ylim(0,3)
			#ax1.set_xlim(0,0.25)
			ax2 = fig.add_subplot(222)
			ax2.plot(freq,esp_vz[:,i])
			ax2.legend(['vz'])
			#ax2.set_ylim(0,3)
			#ax2.set_xlim(0,0.25)
			ax3 = fig.add_subplot(223)
			ax3.plot(freq,esp_vx[:,i])
			ax3.legend(['vx'])
			#ax3.set_ylim(0,3)
			#ax3.set_xlim(0,0.25)
			ax4 = fig.add_subplot(224)
			ax4.plot(freq,esp_vy[:,i])
			ax4.legend(['vy'])
			#ax4.set_ylim(0,3)
			#ax4.set_xlim(0,0.25)

			plt.savefig('Fig_ok/espe_' + day + '_' + str(i) + '.png')

		#evolspec
        fig = plt.figure(figsize=(15,9))
        ax1 = fig.add_subplot(411)
        ax1.contourf(range(esp_pr.shape[1]),freq,esp_pr,100)
        ax1.set_xticklabels(ax1.get_xticklabels(), visible=False)
        ax1.grid()
		#ax1.set_axes('tight')
        ax1.set_ylim(0.04,0.25)
        ax1.set_ylabel('Freq. (Hz)')

		#ax1.set_xticklabels(ax.get_xticks(), adcp.index.astype(str),  fontsize=10, rotation=5)

        ax2 = fig.add_subplot(412)
        ax2.plot(range(len(hm0)),hm0)
        ax2.set_xticklabels(ax2.get_xticklabels(), visible=False)
        ax2.grid()
        ax2.set_ylim(0,2)
        ax2.set_ylabel('Hs (m)')

        ax3 = fig.add_subplot(413)
        ax3.plot(range(len(tp)),tp,'o')
        ax3.set_xticklabels(ax3.get_xticklabels(), visible=False)
        ax3.set_ylim(5,20)
        ax3.grid()
        
        ax3.set_ylabel('Tp (s)')

        ax4 = fig.add_subplot(414)
        ax4.plot(range(len(dp)),dp,'bo')
		#ax4.plot(adcp.index,adcp[' meandir'],'r.')
        ax4.grid()
        ax4.set_ylabel('Dp (graus)')
        ax4.set_yticks(range(0,405,45))
        ax4.set_ylim(100,250)
        
        plt.savefig('Fig_ok/evolspec_' + day + '.png')
        
        
        plt.close('all')

plt.show()
