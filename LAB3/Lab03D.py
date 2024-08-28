E_number = input("Enter the last three digits of your student registration number: ")

t = 0
s = [t := t + int(i) for i in E_number]
n = s[-1]  
print(f"Sum of the digits: {n}")


phi = (1 + 5**0.5) / 2
phi_ = (1 - 5**0.5) / 2


fibb = (phi**n - phi_**n) / (5**0.5)

print(f'The Fibonacci number at position {n} is: {int(fibb)}')
