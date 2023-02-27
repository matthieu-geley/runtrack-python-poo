class Cercle:

	def __init__(self, rayon):
		self.rayon = rayon


	def changerRayon(self, nouveauR):
		self.rayon = nouveauR


	def circonference(self):
		self.circonference = 2 * 3.14 * self.rayon


	def aire(self):
		self.aire = 3.14 * self.rayon * self.rayon


	def diametre(self):
		self.diametre = self.rayon * 2


	def afficherInfos(self):
		print(self.rayon)
		print(self.diametre)
		print(self.aire)
		print(self.circonference)

cercle4 = Cercle(4)
cercle4.rayon()
cercle4.aire()
cercle4.diametre()
cercle4.circonference()
cercle4.afficherInfos()