
"""
Created on January 2020
@author: carlopasquinucci : carlo.a.pasquinucci@gmail.com
"""

"""
Instruction:
1)Fill the data in Initial_Data.data
2)Run Run.py
3)Read the results on Results.dat
"""

print("\n")
print("#########################################################")
print("######                                            #######")
print("######      Calcolus of k epsilon omega           #######")
print("######                                            #######")
print("#########################################################")
print("\n")

#Read data from file

f = open("Initial_Data.dat", "r")

i=0
while (i< 15):
	test=f.readline()
	i= i+1
	
Velocity=float(f.readline())

empty=f.readline()
empty=f.readline()
empty=f.readline()
TurbuLevel=float(f.readline())

empty=f.readline()
empty=f.readline()
empty=f.readline()
TurbuLength=float(f.readline())

f.close()

#Calculus of k omega epsilon

k=(3/2)**(1/2)*(Velocity*TurbuLevel*TurbuLength)
epsilon=3/2*(Velocity*TurbuLevel)**2
omega=epsilon**(1/2)*TurbuLength

#Print on file
F=open("Results","w") 
F.write("k="+str(k)+"\n")
F.write("epsilon="+str(epsilon)+"\n")
F.write("omega="+str(omega)+"\n")

F.close()
print("")
print("Results printed in Results.dat")