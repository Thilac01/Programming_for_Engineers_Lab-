# Power_&_Energy calculation
# CO1010 : Lab 04
# Date : 05/09/2024

# Define funtion for calculating power and Energy

def calculate_power(V, I):
    return V * I

def calculate_energy(V, I, t):
    power = calculate_power(V, I)
    energy = (power * t) / 1000 
    return energy

# get multiple input at a time as Float
V, I, t = map(float, input("Enter the voltage (V), current (I), and time in hours (t) separated by commas: ").split(','))

power = calculate_power(V, I)
energy = calculate_energy(V, I, t)


# Display the output 
print(f"Power consumed by {V}V and {I}A load is: {power} W")
print(f"Energy consumed over {t} hours: {energy} kWh")
