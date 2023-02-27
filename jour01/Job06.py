class Animal:
	def __init__(self):
		age = 0
		self.age = age
		prenom = ""
		self.prenom = prenom
		print("L'age de l'Animal", self.age, "ans")


	def viellir(self):
		self.age += 1
		print("L'age de l'Animal", self.age, "ans")


	def nommer(self, prenom):
		self.prenom = prenom
		print("L'animal se nomme", self.prenom)



Animal1 = Animal()
Animal1.viellir()
Animal1.nommer("Luna")