# Cisco config app

# Gets the questions done so we can then know what they need to configure
# .lower() sets the answers to all lowercase
ConfIP = input("Do you want to configure the IP?: ").lower()
EnPass = input("Do you want to configure the enable password?: ").lower()
ConPass = input("Do youw ant to configuere the console password?: ").lower()
SshPass = input("Do you want to configure the Telnet / SSH password?: ").lower()

if ConfIP == "yes":
    outIP = input("What should the outside IP be?: ")

if EnPass == "yes":
    enablePass = input("What should the enable password be?: ")

if ConPass == "yes":
    ConsolePass = input("What should the console password be?: ")

if SshPass == "yes":
    TelnetPass = input("What should the Telnet / SSH password be?: ")
