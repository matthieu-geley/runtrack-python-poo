class Operation:

	def __init__(self):
		self.nombre1 = 25541
		self.nombre2 = 455120
#		print('Le nombre1 est', self.nombre1)
#		print('Le nombre2 est', self.nombre2)

	def addition(self):
		self.resultat = self.nombre1 + self.nombre2
		print('Le résultat est', self.resultat)

Operation1 = Operation()
Operation1.addition()