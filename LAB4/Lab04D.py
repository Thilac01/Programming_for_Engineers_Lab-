# Deflaction_in_Beams
# CO1010 : Lab 04
# Date : 05/09/2024

# Define the variables
W = 10000
E = 210*10e7
I = 8*10e-6

# Define the funtion for calculating deflaction
def deflaction(W,E,I,L):
    return(((5*W*L**4)/(384*E*I))*10e2)



#Read and unpack the text file and store as array
with open("beamdata.txt", "r") as file:
    data  = file.readlines()
    beam_Length = [float(line.strip())for line in data]
    Deflaction = [deflaction(W,E,I,float(line.strip())) for line in data]


#Create and append output data as a text file
for i in range(len(beam_Length)):
    with open("beam_deflections.txt", "a") as output:
     output.write(f" Beam Length: {beam_Length[i]} m  ,  Deflection: {Deflaction[i]:.5f} mm\n")

