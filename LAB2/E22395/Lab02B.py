# Determine the nature of a fluid flow
# CO1010 : Lab 02
# Date : 15/08/2024

# Read the Reynolds number  as float inputs
Re = float(input("Enter the Reynolds number ( Re ): "))

#check the coditions
if Re <= 2300:
    state = 'Laminar Region'
elif 2300< Re <= 4000:
    state = 'Transition Region'
else:
    state = "Turbulent Region"

#Print the output
print(f"The fluid is in : {state}")