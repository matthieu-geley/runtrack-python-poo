class Personnage:

	def __init__(self, X, Y):
		self.matrice = [[1,2,3],[4,5,6],[7,8,9]]
		self.X = X
		self.Y = Y
		self.matriceXY = self.matrice[self.X][self.Y]


	def haut(self):
		self.X -= 1
		self.matriceXY = self.matrice[self.X][self.Y]


	def bas(self):
		self.X += 1
		self.matriceXY = self.matrice[self.X][self.Y]


	def gauche(self):
		self.Y -= 1
		self.matriceXY = self.matrice[self.X][self.Y]


	def droite(self):
		self.Y += 1
		self.matriceXY = self.matrice[self.X][self.Y]


	def position(self):
		posXY = (self.X, self.Y)
		print(posXY)


Joueur1 = Personnage(2, 0)
Joueur1.position()
Joueur1.haut()
Joueur1.position()
Joueur1.droite()
Joueur1.position()