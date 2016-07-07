outip = input("Would you like to configure the IP?: ").lower()

ipadd = "ip address "

if outip == "yes":
    outsideIP = input("What should the IP be?: ")
    subnetMask = input("What should the subnet mask be?: ")
else:
    ipadd = "!"
    subnetMask = "!NO SUBNET WAS CHOSEN"
    outsideIP = "NO IP WAS CHOSEN\n"

print("\nint f0/1\n" + ipadd + outsideIP + " " + subnetMask)