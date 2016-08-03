# Cisco config app

# IMPORTS
import ipaddress

# GLOBAL FUNCS
def errorfunc():
    outIP = input("What should the outside IP be?: ")

    IpError = outIP.count('.')

    if IpError == 3:
        print("Good IP")
    else:
        errorfunc()



# GLOABL VARIABLES
IpAdd = "ip address "
inter = "interface "
enpassword = "enable password "
ConPassword = "line vty 0 "
SshPassword = "line vty 0 4 "


# Gets the questions done so we can then know what they need to configure
# .lower() sets the answers to all lowercase
ConfIP = input("Do you want to configure the IP?: ").lower()
EnPass = input("Do you want to configure the enable password?: ").lower()
ConPass = input("Do you want to configuere the console password?: ").lower()
SshPass = input("Do you want to configure the Telnet / SSH password?: ").lower()
Layer3Switch = input("Type yes for Layer 3 switch: ").lower()
VTPmode = input("Type yes for VTP client mode, anything else will be transparent mode: ").lower()

# What the else statements do is if the user did not say yes it does a comment in the Cisco IOS
if ConfIP == "yes":
    port = input("What is the port?: ")
    outIP = input("What should the outside IP be?: ")

    ipaddress.ip_address(outIP)

    # IpError = outIP.count('.')
    #
    # if IpError == 3:
    #     print("Good IP")
    # else:
    #     errorfunc()

    subnetMask = input("What is the subnet mask?: ")
    SubnetError = subnetMask.count('.')

    ipaddress.ip_address(subnetMask)

    # if SubnetError > 3:
    #     print("Please enter a valid subnet mask")
    #     subnetMask = input("What is the subnet mask?: ")

else:
   inter = "!"
   port = "NO PORT WAS CONFIGURED"
   outIP = " WAS"
   IpAdd = "!NO IP"
   subnetMask = "CONFIGURED"

if EnPass == "yes":
    enablePass = input("What should the enable password be?: ")
else:
    enpassword = "!"
    enablePass = "ENABLE PASSWORD WAS NOT CHOSEN"

if ConPass == "yes":
    ConsolePass = input("What should the console password be?: ")
else:
    ConPassword = "!"
    ConsolePass = "CONSOLE PASSWORD WAS NOT CHOSEN"

if SshPass == "yes":
    TelnetPass = input("What should the Telnet / SSH password be?: ")
else:
    SshPassword = "!"
    TelnetPass = "SSH / TELNET PASSWORD WAS NOT CHOSEN"

if Layer3Switch == "yes":
    L3Route = input("What is the Default Gateway? ")
else:
    L2Route = input("What is the Default Gateway? ")

hostname = input("What is the hostname? ")

domainname = input("What is the domain name? ")

# DEBUG
print("\nThe config: \n!")
testConfig = inter + port + "\n" + IpAdd + outIP + " " + subnetMask + "\n!\n" + enpassword + enablePass + "\n" + ConPassword + ConsolePass + "\n" + SshPassword + TelnetPass
print(testConfig)

# Start config
print ("hostname " + hostname)
print ("ip domain-name " + domainname)

if VTPmode == "yes":
    print ("vtp mode client")
else:
    print ("vtp mode transparent")

# Base config

print("service tcp-keepalives-in")
print("service tcp-keepalives-out")
print("service timestamps debug datetime msec localtime show-timezone")
print("service timestamps log datetime msec localtime show-timezone")
print("service password-encryption")
print("service sequence-numbers")
print("exception crashinfo maximum files 2")
print("warm-reboot count 10 uptime 5")
print("")

