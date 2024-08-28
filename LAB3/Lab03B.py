
connection_type = str(input("Enter the type of the connection (S for Series, P for Parallel): "))

def resistance_array(resistance):
    resistances = []
    resistances.append(resistance) 
    return resistances 

if connection_type == 's' or connection_type == "S":
    resistances = []
    while True:
        value_of_resistance = float(input("Enter the value of resistance (or '0' to end): "))
        if value_of_resistance == 0:
            break 
        resistances.append(value_of_resistance) 
    total_resistance = sum(resistances) 
    print(f"Equivalent resistance in series: {total_resistance} ohms")

elif connection_type == 'p' or connection_type == "P":
    resistances = []
    while True:
        value_of_resistance = float(input("Enter the value of resistance (or '0' to end): "))
        if value_of_resistance == 0:
            break 
        resistances.append(value_of_resistance) 

    if resistances:
        total_reciprocal = sum(1/r for r in resistances)
        total_resistance = 1 / total_reciprocal
        print(f"Equivalent resistance in parallel: {total_resistance} ohms")
    else:
        print("No resistances entered.")

else:
    print("Invalid connection type. Please enter 'S' for Series or 'P' for Parallel.")
