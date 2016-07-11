def fuckfunc():
    outIP = input("What is your IP?: ")

    IpError = outIP.count('.')

    if IpError == 3:
        print("Good IP")
    else:
        fuckfunc()



outIP = input("What is your IP?: ")

IpError = outIP.count('.')

if IpError == 3:
    print("Good IP")
else:
    fuckfunc()

print("\nPORT: f0/1\n IP ", outIP + "\n")