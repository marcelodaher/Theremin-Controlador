# PONG NO TERMINAL #
# a ideia e ter uma taxa de atualizacao alta, imagino que por volta de 30hz, do jogo
# entao, a cada 1/30s atualizar uma variavel com a frequencia do ocilador 'theremistico', que daria a posicao da raquete

# tamanho do terminal: 80x24

# biblioteca SoundAnalyse pelo pacote 'import analyse'
#import analyse
# soundAnalyse nao instalou, usando o aubio
import aubio

# importando o audio do microfone pelo 'pyaudio'
import pyaudio

# essa agora e pra converter o som pra um array numerico pra jogar no analyse
import numpy
import os
import sys
import time

#funcao que vai imprimir a tela
def imprime_tela(placar, raquetes, tamanho_raquete, bola):
	os.system('clear')
	print "user {} x {} machine" .format(placar[0],placar[1])
	for t in range(80):
		sys.stdout.write('_'),
	print
	n_de_linhas=40
	for linha in range(n_de_linhas):
		if linha != bola[0]:
			if linha >= raquetes[0] and linha<raquetes[0]:
				sys.stdout.write("|")
			else:
				sys.stdout.write(" ")

			for t in range(78):
				sys.stdout.write(' '),

			if linha >= raquetes[1] and linha<raquetes[1]:
				print("|")
			else:
				print(" ")
		else:
			if bola[1]==0:
				print "POINT USER"
				placar[0]=placar[0]+1
			elif bola[1]==79:
				print "POINT MACHINE"
				placar[1]=placar[1]+1
			else:
				if linha >= raquetes[0] and linha<raquetes[0]:
					sys.stdout.write("|")
				else:
					sys.stdout.write(" ")

				for x in range(bola[2]-2):
					sys.stdout.write(" ")
				sys.stdout.write("O")
				for x in range(78-bola[2]):
					sys.stdout.write(" ")

				if linha >= raquetes[1] and linha<raquetes[1]:
					print("|")
				else:
					print(" ")
				

#variaveis no estilo [user,machine]
placar=[0,0]
raquetes=[40,40]
tamanho_raquete=[10,10]
gol=0

#funcao time da biblioteca time pega o tempo do sistema
#usar para definir a taxa de atualizacao do jogo
time = time.time()

bola = [20,40] #[linha,coluna]

if gol == 0 and placar[0]<5 and placar[1]<5:
	imprime_tela(
	



