class Cercle:

	def __init__(self, rayon):
		self.rayon = rayon


	def changerRayon(self, nouveauR):
		self.rayon = nouveauR


	def circonference(self):
		self.circonference = 2 * 3.14 * self.rayon
		return self.circonference


	def aire(self):
		self.aire = 3.14 * self.rayon * self.rayon
		return self.aire


	def diametre(self):
		self.diametre = self.rayon * 2
		return self.diametre


	def afficherInfos(self):
		print("Le cercle a un rayon de", self.rayon)
		print("Le cercle a un diamètre de", self.diametre)
		print("Le cercle a une aire de", self.aire)
		print("Le cercle a une circonférence de", self.circonference)

cercle4 = Cercle(4)
print("Cercle de 4")
cercle4.circonference()
cercle4.aire()
cercle4.diametre()
cercle4.afficherInfos()
print()
print("Cercle de 7")
cercle7 = Cercle(4)
cercle7.changerRayon(7)
cercle7.circonference()
cercle7.aire()
cercle7.diametre()
cercle7.afficherInfos()