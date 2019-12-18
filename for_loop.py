
device=["R1","R2","R3","S1","S2"]
for i in device:
    print(i)
for i in device:
    if "R" in i:
        print(i)
switches=[]
for i in device:
    if "S" in i:
        switches.append(i)
print (switches)
