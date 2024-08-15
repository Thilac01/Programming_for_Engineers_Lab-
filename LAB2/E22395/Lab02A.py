# Tempreature unit converter
# CO1010 : Lab 02
# Date : 15/08/2024

# Read the celsius_temp  as float inputs
Tc = float(input("Enter temperature in Celsius: "))

# Calculations
Tf = (9/5)*Tc+32
Tk = Tc + 273.15

# Read the converting_factor as string input
converting_factor = str(input("Do you want to convert K or F ?: "))


# check the condition
if converting_factor == "K"  or converting_factor == "k" :
    # print the output
    print(f" The temperature value in Fahrenheit is {Tk:0.2f}.")
else:
    if converting_factor == "F" or converting_factor == "f":
        # print the output
        print(f"The temperature value in Fahrenheit is {Tf:0.2f}.")
        
