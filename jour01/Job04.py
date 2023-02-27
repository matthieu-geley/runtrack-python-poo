class Personne:

	def __init__(self, prenom, nom):
		self.nom = nom
		self.prenom = prenom

	def SePresenter(self):
		print('Je suis', self.prenom, self.nom)

presenter1 = Personne("John", "Doe")
presenter2 =Personne("Jean", "Dupond")
presenter1.SePresenter()
presenter2.SePresenter()