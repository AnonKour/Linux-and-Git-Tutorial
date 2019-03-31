#This program calculates the Surface area of different shapes. 
# Enclosed volume and Surface area?
import os
import codecs
import sys

import cube
import sphere

# The surface area formula can be found at https://en.wikipedia.org/wiki/Surface_area.

shapeCategoriesDisplay = { 0 : 'cube',
					#1 : 'cuboid',
					#2 : 'triangular_Prism',
					#3 : 'all_Prisms',
					4 : 'sphere'
					#5 : 'spherical_Lune',
					#6 : 'torus',
					#7 : 'closed_Cylinder',
					#8 : 'full_Surface_Area_Cone',
					#9 : 'pyramid',
					#10 : 'square_Pyramid',
					#11 : 'rectangular_Pyramid',
					#12 : 'tetrahedron'
}


def cube_SurfaceArea():
	return cube.calculate_SA()
	
def sphere_SurfaceArea():
	return sphere.calculate_SA()

'''	
def cuboid_SurfaceArea():
	
def triangular_Prism_SurfaceArea():
	
def all_Prisms_SurfaceArea():
	

	
def spherical_Lune_SurfaceArea():
	
def torus_SurfaceArea():
	
def closed_Cylinder_SurfaceArea():
	
def full_Surface_Area_Cone_SurfaceArea():
	
def pyramid_SurfaceArea():
	
def square_Pyramid_SurfaceArea():
	
def rectangular_Pyramid_SurfaceArea():
	
def tetrahedron_SurfaceArea():

'''
shapeCategories = { 0 : cube_SurfaceArea,
					#1 : cuboid_SurfaceArea,
					#2 : triangular_Prism_SurfaceArea,
					#3 : all_Prisms_SurfaceArea,
					4 : sphere_SurfaceArea
					#5 : spherical_Lune_SurfaceArea,
					#6 : torus_SurfaceArea,
					#7 : closed_Cylinder_SurfaceArea,
					#8 : full_Surface_Area_Cone_SurfaceArea,
					#9 : pyramid_SurfaceArea,
					#10 : square_Pyramid_SurfaceArea,
					#11 : rectangular_Pyramid_SurfaceArea,
					#12 : tetrahedron_SurfaceArea
}

def main():

	print("\nChose one of the following shapes that you want to calculate its surface area:\n")
	for i in shapeCategoriesDisplay:
		print("Type " +str(i)+ " for " + str(shapeCategoriesDisplay[i]))

	print("\n")
	answer = 100
	while not (answer < 12 and answer >=0):

		user_input = input("Chose one of the above.\n")
		try:
			answer = int(user_input)
		except ValueError:
			print("That's not an integer!")

	print("The surface area is: " + str(shapeCategories[answer]()) + " cm^2.\n")
main()