# CODIGO RODA POR TRAS
# CODIGO DOS OBJETOS

from os import system # Inclue o codigo para limpar a tela  (mesma coisa que #inclde <stdlin.h>)
from ReadArrow import readKey # Inclue o codigo do leitor de teclas


"""
class YX:
	docstring for Position
	def __init__(self, y:int, x:int):
		self.x = x
		self.y = y
"""
class Player: # Objeto JOGADOR
	def __init__(self):#, MapList:str):
		self.First = True # Teste para se a primeira fez iniciando
		#setPosition()
		pass

	def setPosition(self, X=0, Y=0):
		if self.First : # Caso for a primeira vez iniciando, ele coloca a posiçao do jogador como a primeira possivel
			self.First = False
			for i in range(0, len(self.Positions)):
				if self.Positions[i] != []:
					self.Y = i
					self.X = self.Positions[i][0]

					break;
		else: # Se nao
			
			if self.isPossible(Y, X): # ele testa se a posiçao passada é possivel
				self.X = X
				self.Y = Y	
				# E se sim a define
		pass 

	def isPossible(self, Y, X):# ele testa se a posiçao passada é possivel
		for i in range(0, len(self.Positions)):
			if self.Positions[i] != []:
				for j in range(0, len(self.Positions[i])):
					if Y == i and self.Positions[i][j] == X:
						return True
		return False
		

	def definePositions(self, PositionsMap:list): # Atribui a variavel 'Positions' as posiçoes possiveis 
		self.Positions = PositionsMap
		pass

class Game:
	"""docstring for Game"""
	def __init__(self):
		self.GameOver = False # Variavel para teste de final de jogo
		self.First = True # Variavel para teste se é a primeira vez executando o jogo
		self.P = Player() # Cria o jogador
		pass

	def ClearScreen(self): # Limpa a tela
		system('cls')
		pass

	def ShowMap(self):# Mostra o Mapa
		self.ClearScreen()
		print(self.StrMap)
		pass

	def toStr(self): # Transforma a MATRIZ para STRING
		self.StrMap = ''.join(''.join(i + ['\n']) for i in [j for j in self.MapList])
		pass


	def UpdateMap(self): # Atualiza o Mapa
		self.toStr()
		pass

	def toList(self,Map:str): # Transforma o mapa STRING para MATRIZ
		vetor = [[j for j in i]for i in Map.split('\n')]
		return vetor

	def setPositions(self):
		PositionsMap = [[x  for x in range(0, len(self.MapList[y])) if ' ' in self.MapList[y][x]] for y in range(0, len(self.MapList))] 
		self.P.definePositions(PositionsMap)
		pass
	
	def defineMap(self, Map:str): # Difine o mapa passado pelo codigo principal
		self.MapList = self.toList(Map)
		pass

	def clearPostion(self): # Limpa a posiçao antiga do jogador
		self.MapList[self.P.Y][self.P.X] = ' '
		pass

	def PositionPlayer(self, X=0, Y=0):# Edita o mapa para indicar o jogodor com o caractere '*'

		self.MapList[self.P.Y][self.P.X] = '*'
		pass

	def Start(self): # Inicia o jogo
		while not self.GameOver:
			try:
				
				if self.First: # Teste para ver se o jogo iniciou somente uma vez
					self.setPositions() #Define as posiveis posiçoes do jogodor
					self.P.setPosition() # Inicia a posiçao do jogados
					self.PositionPlayer() 
					self.UpdateMap() # Atualiza o mapa
					self.ShowMap() 
					self.First = False
					pass
				
				#self.P.setPosition()
				move, key = readKey() # Le qual tecla foi preciona
				if move != 0 and key != 0:
					self.clearPostion()
					if move == 1 :
						self.P.setPosition(self.P.X, self.P.Y + key) # Modifica a posicao do eixo Y
					elif move == 2:
						self.P.setPosition(self.P.X + key, self.P.Y)# Modifica a posicao do eixo X
					self.PositionPlayer()
					self.UpdateMap()

					self.ShowMap()
					#print(self.P.Y, self.P.X)
				if self.P.Y == 15 and self.P.X == 47: #  Se posiçao do jogador for Y : 15 X : 47 (ultima posiçao do mapa) ele termina o jogo
					self.GameOver = True
				
			except KeyboardInterrupt:
				self.GameOver = True
				self.ClearScreen()
			
			pass
		self.ClearScreen()