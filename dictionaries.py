
ipAddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
print(type(ipAddress))
print(ipAddress)
print(ipAddress["R1"])
ipAddress["S1"]="10.1.1.10"
print(ipAddress)
print("R3" in ipAddress)
