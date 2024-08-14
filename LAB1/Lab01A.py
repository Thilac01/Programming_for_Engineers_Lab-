# Greetings
# CO1010 : Lab 01
# Date : 08/08/2024

#Print the Header details
print('Enter your details\n'+'- '*22 )
# Read the names as string inputs
first_name = input("First name: ")
last_name = input("Last name: ")

# Read the Age as int inputs
age = int(input("Age: "))

print("Date of birth: ")
# Read the dates as string inputs
month = input("Month ? ")
days = input("Days ? ")
year = input("Year ? ")

#Print the output
print(f'Greetings to {first_name} {last_name}, aged {age}, born on {month} {days}, {year}! ')
