# Finding the volume of a cone
# CO1010 : Lab 01
# Date : 08/08/2024


# Read the numbers as float inputs
radius = float(input('Enter the raduis: '))
height = float(input('Enter the height: '))

# Define the constant
pi =  3.1415927 

#Calculations
v = (1/3)*pi*abs(height)*radius**2

 #Print the output
print(f"The volume of the cone is {v:8.3f}") 
