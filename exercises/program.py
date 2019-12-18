model1 = open("model1.pdb", "r")
model2 = open("model2.pdb", "r")
l1 = []
l2 = []
l3 = []
for line in model1:
    if "CA" in line:
        l1.append(line[32:55].split())
     
for line in model2:
    if "CA" in line:
        l2.append(line[32:55].split())



from math import *
xsum = 0
for lista in l3:
    for sottolista in lista:
        xsum += float(sottolista)
print("\n")

x = 0
for i in range(len(l1)):
    for j in range(3):
        cord1=float(l1[i][j])
        cord2=float(l2[i][j])
        t=cord1-cord2
        t=t**2
        x=x+t
rmsd=math.sqrt((x/100))
print(rmsd)



