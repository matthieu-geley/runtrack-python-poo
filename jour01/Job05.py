class Point:

	def __init__(self, x, y):
		self.pointx = x
		self.pointy = y


	def afficherLesPoints(self):
		print('Les coordonées en X et en Y sont :', self.pointx, self.pointy)


	def afficherX(self):
		print('La coordonée en X est :',self.pointx)


	def afficherY(self):
		print('La coordonée en Y est :',self.pointy)


	def changerX(self, nouveauX):
		self.pointx = nouveauX


	def changerY(self, nouveauY):
		self.pointy = nouveauY

Point1 = Point(5, 20)
Point1.afficherLesPoints()
Point1.afficherX()
Point1.changerY(57)
Point1.afficherY()