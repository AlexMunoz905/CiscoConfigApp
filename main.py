inputvar = input("Nexus, ASA, Catalyst or Router: ").lower()

if inputvar == "catalyst":
    import Catalyst
elif inputvar == "nexus":
    import nexus
elif inputvar == "asa":
    print("nice man")
elif inputvar == "router":
    print("sweet man")
else:
    print("boi")