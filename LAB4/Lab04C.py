# ladder_against_the_Wall
# CO1010 : Lab 04
# Date : 05/09/2024

# import the inbulid math module
import math as m

# get the variable as a float 
length , angle = map(float,input("Enter the length of the ladder (in meters) and the angle (in degrees):").split(','))

# calcultaion part
def ladder_against_the_Wall(length,angle):
    return(length*(m.sin(m.radians(angle))))
# diplay the output
print(f"Height of the ladder against the wall: {ladder_against_the_Wall(length,angle):.2f} meters")