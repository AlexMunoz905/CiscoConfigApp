# Cisco config app

# IMPORTS
import ipaddress

# GLOBAL FUNCS
def errorfunc():
    MngtIP = input("What should the IP be?: ")

    IpError = MngtIP.count('.')

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
# ConfIP = input("Do you want to configure the IP?: ").lower()
# EnPass = input("Do you want to configure the enable password?: ").lower()
# ConPass = input("Do you want to configuere the console password?: ").lower()
# SshPass = input("Do you want to configure the Telnet / SSH password?: ").lower()
print ("\n")
Layer3Switch = input("Type yes for Layer 3 switch, anything else will be Layer 2: ").lower()
VTPmode = input("Type yes for VTP client mode, anything else will be transparent mode: ").lower()
SNMPCom = input("Adding SNMP Community?: ").lower()

# What the else statements do is if the user did not say yes it does a comment in the Cisco IOS
# if ConfIP == "yes":
#    port = input("What is the port?: ")
#    MngtIP = input("What should the IP be?: ")

#    ipaddress.ip_address(MngtIP)

    # IpError = outIP.count('.')
    #
    # if IpError == 3:
    #     print("Good IP")
    # else:
    #     errorfunc()

#    subnetMask = input("What is the subnet mask?: ")
#    SubnetError = subnetMask.count('.')

#    ipaddress.ip_address(subnetMask)

    # if SubnetError > 3:
    #     print("Please enter a valid subnet mask")
    #     subnetMask = input("What is the subnet mask?: ")

# else:
#  inter = "!"
#   port = "NO PORT WAS CONFIGURED"
#   MngtIP = " WAS"
#   IpAdd = "!NO IP"
#   subnetMask = "CONFIGURED"

enablePass = input("What should the enable password be?: ")

# if ConPass == "yes":
#   ConsolePass = input("What should the console password be?: ")
# else:
#    ConPassword = "!"
#    ConsolePass = "CONSOLE PASSWORD WAS NOT CHOSEN"

# if SshPass == "yes":
#    TelnetPass = input("What should the Telnet / SSH password be?: ")
# else:
#   SshPassword = "!"
#    TelnetPass = "SSH / TELNET PASSWORD WAS NOT CHOSEN"

hostname = input("What is the hostname? ")

domainname = input("What is the domain name? ")

VTPpass = input("What is the VTP password? ")

MngtVLAN = input("What is the Management VLAN #? ")

MngtVLANname = input("what is the Managment VLAN name? ")

MngtIP = input("What should the IP be?: ")

ipaddress.ip_address(MngtIP)

    # IpError = outIP.count('.')
    #
    # if IpError == 3:
    #     print("Good IP")
    # else:
    #     errorfunc()

subnetMask = input("What is the subnet mask?: ")
SubnetError = subnetMask.count('.')

ipaddress.ip_address(subnetMask)

# print ("ip address " + MngtIP + subnetMask)
if Layer3Switch == "yes":
    L3Route = input("What is the Default Gateway? ")
else:
    L2Route = input("What is the Default Gateway? ")

if SNMPCom == "yes":
    SNMPCommunity = input("What should the SNMP Community be?: ")

# DEBUG
print("\nThe config: \n!")
# testConfig = inter + port + "\n" + IpAdd + outIP + " " + subnetMask + "\n!\n" + enpassword + enablePass + "\n" + ConPassword + ConsolePass + "\n" + SshPassword + TelnetPass
# print(testConfig)

# Start config
print ("hostname " + hostname)
print ("ip domain-name " + domainname)

if VTPmode == "yes":
    print ("vtp mode client")
else:
    print ("vtp mode transparent")

print ("vtp password "+ VTPpass)

print ("vlan " + MngtVLAN)
print ("name " + MngtVLANname)
print ("interface vlan " + MngtVLAN)
print ("ip address " + MngtIP + " " + subnetMask)
if Layer3Switch == "yes":
    print ("ip route 0.0.0.0 0.0.0.0 " + L3Route)
    print ("ip routing")
else:
    print ("ip default-gateway " + L2Route)
    print ("no ip routing")
if SNMPCom == "yes":
    print ("snmp-server community "+ SNMPCommunity)

# Base config

import base-cat

