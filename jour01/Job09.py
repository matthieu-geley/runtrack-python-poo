class Produit:

	def __init__(self, nom, prixHT, TVA):
		self.nom = nom
		self.prixHT = prixHT
		self.TVA = TVA


	def modifierPrix(self, nouveauPrix, nouvelleTVA):
		self.prixHT = nouveauPrix
		self.TVA = nouvelleTVA
		return self.prixHT, \
			self.TVA


	def CalculerPrixTTC(self):
		self.prixTTC = self.prixHT * self.TVA / 100 + self.prixHT
		return self.prixTTC


	def modifierNom(self, nouveauNom):
		self.nom = nouveauNom
		return self.nom


	def afficher(self):
		return self.nom, \
			self.prixHT, \
			self.prixTTC, \
			self.TVA

Produit1 = Produit("Pomme", 12, 5)
Produit2 = Produit("Chaise", 25, 20)

Produit1.CalculerPrixTTC()
print(Produit1.afficher())

Produit2.CalculerPrixTTC()
print(Produit2.afficher())

Produit2.modifierNom("Table")
Produit2.modifierPrix(75,14)
print(Produit2.afficher())