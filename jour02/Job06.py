class Commande:

	def __init__(self, commande, liste, status):
		self.__commande = commande
		self.__liste = liste
		if status == 1:
			etat = "en cours"
		elif status == 2:
			etat = " terminée"
		else:
			etat = "annulée"
		self.__status = etat


	def ajouterPlat(self):
		