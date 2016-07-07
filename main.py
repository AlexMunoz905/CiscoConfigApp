# Cisco config app

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
    subnetMask = input("What is the subnet mask?: ")
else:
    port = "!"
    outIP = "!"
    subnetMask = "!"

if EnPass == "yes":
    enablePass = input("What should the enable password be?: ")
else:
    enablePass = "!"

if ConPass == "yes":
    ConsolePass = input("What should the console password be?: ")
else:
    ConsolePass = "!"

if SshPass == "yes":
    TelnetPass = input("What should the Telnet / SSH password be?: ")
else:
    TelnetPass = "!"



# DEBUG
print("\nThe config: \n!")
testConfig = "interface " + port + "\nip address " + outIP + " " + subnetMask + "\n!\nenable password " + enablePass + "\nline vty 0 " + ConsolePass + "\nline vty 0 4 " + TelnetPass
print(testConfig)

# Base config
print("service tcp-keepalives-in")
print("service tcp-keepalives-out")
print("service timestamps debug datetime msec localtime show-timezone")
print("service timestamps log datetime msec localtime show-timezone")
print("service password-encryption")
print("service sequence-numbers")
