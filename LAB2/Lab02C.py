# Grading
# CO1010 : Lab 02
# Date : 15/08/2024

# Read the marks  as float inputs
marks= float(input("Enter the marks :"))

gs = str(input("Enter the Grading schema method: ")).upper()
#check the coditions
if gs == "SG":
    if 90< marks <=100:
        grade = "A"
    elif 80< marks <=89:
        grade = "B"        
    elif 70< marks <=79:
        grade = "C"
    elif 60< marks <=69:
        grade = "D"
    elif 0< marks <=59:
        grade = "F"
    print(f"user grade is{grade}")
elif gs == "PMG":
    if 97< marks <=100:
        grade = "A+"
    elif 93< marks <=96:
        grade = "A"        
    elif 90< marks <=92:
        grade = "A-"
    elif 87< marks <=89:
        grade = "B+"
    elif 83< marks <=86:
        grade = "B"
    elif 80< marks <=82:
        grade = "B-"        
    elif 77< marks <=79:
        grade = "C+"
    elif 73< marks <=76:
        grade = "C"
    elif 70< marks <=72:
        grade = "C-"
    elif 67< marks <=69:
        grade = "D+"        
    elif 63< marks <=66:
        grade = "D"
    elif 60< marks <=62:
        grade = "D-"
    elif 0< marks <=59:
        grade = "F"
    
    
    #Print the output
    print(f"Your grade in {gs} Scheme is {grade}")