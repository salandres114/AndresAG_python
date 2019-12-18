
hostnames=["R1","R2","R3","S1","S2"]
print(type(hostnames))
print(len(hostnames))
print(hostnames)
print(hostnames[0])
print(hostnames[-1])
hostnames[0]="RTR1"
print(hostnames)
del hostnames[3]
print(hostnames)
