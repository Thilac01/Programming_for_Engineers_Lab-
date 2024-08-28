x = 5


for i in range(x):
    for j in range(x-(i)):
        print(" ", end='')

    for j in range(i+1):
        print("q", end='')


    for j in range(i+1):
        print("r", end='')

    for j in range(x-(i)):
        print(" ", end='')

    print()

for i in range(x):
    for j in range(i+1):
        print(" ", end='')

    for j in range(x-(i)):
        print("r", end='')

    for j in range(x-(i)):
        print("s", end='')

    for i in range(i+1):
         print(" ", end='')


    print()