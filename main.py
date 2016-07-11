# Cisco config app

# IMPORTS
import ipaddress

# GLOBAL FUNCS
def errorfunc():
    outIP = input("What should the toutside IP be?: ")

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



# DEBUG
print("\nThe config: \n!")
testConfig = inter + port + "\n" + IpAdd + outIP + " " + subnetMask + "\n!\n" + enpassword + enablePass + "\n" + ConPassword + ConsolePass + "\n" + SshPassword + TelnetPass
print(testConfig)

# Base config
print("service tcp-keepalives-in")
print("service tcp-keepalives-out")
print("service timestamps debug datetime msec localtime show-timezone")
print("service timestamps log datetime msec localtime show-timezone")
print("service password-encryption")
print("service sequence-numbers")
