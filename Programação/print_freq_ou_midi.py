#programa pra ler e imprimir a frequencia do microfone dada uma certa taixa de atualizacao

# biblioteca SoundAnalyse pelo pacote 'import analyse'
import analyse

# importando o audio do microfone pelo 'pyaudio'
import pyaudio

# essa agora e pra converter o som pra um array numerico pra jogar no analyse
import numpy
import os
import time

#os.system('clear')

tempo_anterior = 0

while 1 == 1:
	tempo_atual = time.time()
	if tempo_atual - tempo_anterior > 0.02: #atualizacao 30Hz
		print "%.2f" % tempo_atual
		tempo_anterior=tempo_atual

