# Tempreature unit converter
# CO1010 : Lab 02
# Date : 1t5/08/2024

# Read the celsius_temp  as float inputs
celsius_temp = float(input("Enter temperature in Celsius :"))

# Read the converting_factor as string inputs
converting_factor = str(input("Do you want to convert K or F ?:")).upper()




if converting_factor == 'K':
    Tk = celsius_temp + 273.15  # for unit convertion
    #Print the output
    print(f"The temperature value in Kelvin is {Tk:0.2f}")
elif converting_factor == 'F':
    Tf = (9/5)*celsius_temp + 32 # for unit convertion
    #Print the output
    print(f"The temperature value in  Fahrenheit is {Tf:0.2f}")