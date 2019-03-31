#This script calculates the surface area of a cube.

def calculate_SA():
	side = -1
	while not (side > 0):

		user_input = input("Type the side of the cube in cm: ")
		try:
			side = int(user_input)
		except ValueError:
			print("That's not an integer!")
	
	
	return 6*side^2;