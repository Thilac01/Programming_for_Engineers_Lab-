#  Finding the vertical stress s under the centre of a loaded circular area
# CO1010 : Lab 01
# Date : 08/08/2024


# Read the values as floating inputs
q = float(input('Enter the applied load per unit area (pressure): '))
r = float(input('Enter the radius of the circular loaded area: '))
z = float(input('Enter the depth below the center of the loaded area: '))

s = q*(1-1/(((r**2/z**2)+1)**(3/2))) # for calculations

#Print the output
print(f" vertical stress is {s:8.3f}") 
