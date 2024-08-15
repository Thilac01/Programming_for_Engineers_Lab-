# Grading
# CO1010 : Lab 02
# Date : 15/08/2024

# Read the marks  as float inputs
marks= float(input("Enter the marks :"))

gs = str(input("Enter the Grading schema method: "))
#check the coditions
if gs=="SG" or gs == "sg":
    if marks>=90 and marks<=100:
        print("A")
    if marks>=80 and marks<=89:
        print("B")
    if marks>=70 and marks<=79:
        print("C")
    if marks>=60 and marks<=69:
        print("D")
    if marks>=0 and marks<=59:
        print("F")
else:
    if gs=="PMG" or gs == "pmg":
        if marks>=97 and marks<=100:
            print("A+")
        if marks>=93 and marks<=96:
            print("A")
        if marks>=90 and marks<=92:
            print("A-")
        if marks>=87 and marks<=89:
            print("B+")
        if marks>=83 and marks<=86:
            print("B")
        if marks>=80 and marks<=82:
            print("B-")
        if marks>=77 and marks<=79:
            print("C+")
        if marks>=73 and marks<=76:
            print("C")
        if marks>=70 and marks<=72:
            print("C-")
        if marks>=67 and marks<=69:
            print("D+")
        if marks>=63 and marks<=66:
            print("D")
        if marks>=60 and marks<=62:
            print("D-")
        if marks>= 0 and marks<=59:
            print("F")
