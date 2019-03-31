#This script calculates the surface area of a sphere.

pi = 3.14

def calculate_SA():
	radius = -1
	while not (radius > 0):

		user_input = input("Type the radius of the cube in cm: ")
		try:
			radius = int(user_input)
		except ValueError:
			print("That's not an integer!")
	
	
	return 4*pi*(radius^2);