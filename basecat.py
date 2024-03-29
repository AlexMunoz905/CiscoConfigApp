def ourfunctionsucks():

    print("service tcp-keepalives-in")
    print("service tcp-keepalives-out")
    print("service timestamps debug datetime msec localtime show-timezone")
    print("service timestamps log datetime msec localtime show-timezone")
    print("service password-encryption")
    print("service sequence-numbers  ")
    print("exception crashinfo maximum files 2")
    print("! Speed up large configurations when accessed")
    print("parser config cache interface")
    print("parser config partition")
    print("warm-reboot count 10 uptime 5")
    print("exception memory ignore overflow io")
    print("exception memory ignore overflow processor")
    print("!")
    print("!")
    print("!------------UN-NEEDED SERVICES SHUT OFF FOR SECURITY Global Mode ----------------------------")
    print("no service tcp-small-servers")
    print("no service udp-small-servers")
    print("no service pad")
    print("no ip finger")
    print("no service finger")
    print("no ip http server")
    print("no ip http secure-server")
    print("no service config")
    print("!")
    print("!")
    print("!-------------------IP ROUTING COMMANDS -------------------------------------------")
    print("ip routing")
    print("ip cef")
    print("ip classless")
    print("ip subnet-zero")
    print("no ip source-route")
    print("!")
    print("!")
    print("no ip domain-lookup")
    print("ip tcp synwait-time 5")
    print("!")
    print("logging buffered 256000 debugging")
    print("no logging console")
    print("logging monitor critical")
    print("logging trap debugging")
    print("!")
    print("archive")
    print("log config")
    print("logging enable")
    print("logging size 1000")
    print("notify syslog")
    print("hidekeys")
    print("!")
    print("archive")
    print("path flash:BackupConfig")
    print("maximum 7")
    print("write-memory")
    print("!")
    print("no enable password")
    print("")
    print("enable secret -StringHere-")
    print("")
    print("login on-failure log")
    print("login on-success log")
    print("")
    print("!------------------------ SNMP ----------------------------------------------------------")
    print("no snmp-server community public RO")
    print("no snmp-server community private RW")
    print("snmp-server ifindex persist")
    print("")
    print("no banner motd")
    print("banner motd ^")
    print("**********************************************************************")
    print("WARNING: This system is for the use of authorized clients only.")
    print("Individuals using the computer network system without authorization,")
    print("or in excess of their authorization, are subject to having all their")
    print("activity on this computer network system monitored and recorded by")
    print("system personnel.  To protect the computer network system from")
    print("unauthorized use and to ensure the computer network systems is")
    print("functioning properly, system administrators monitor this system.")
    print("Anyone using this computer network system expressly consents to such")
    print("monitoring and is advised that if such monitoring reveals possible")
    print("conduct of criminal activity, system personnel may provide the")
    print("evidence of such activity to law enforcement officers")
    print("Access is restricted to authorized users only. Unauthorized access is")
    print("a violation of state and federal, civil and criminal laws")
    print("**********************************************************************")
    print("^")
    print("")
    print("")
    print("banner exec ^")
    print("**********************************************************************")
    print("                          Company Name")
    print("                          HOST: $(hostname)")
    print("                          Configured for Data and Voice Use")
    print("**********************************************************************")
    print("^")
    print("")
    print("crypto key generate rsa general-keys modulus 2048")
    print("ip ssh time-out 29")
    print("ip ssh authentication-retries 2")
    print("ip ssh version 2")
    print("ip ssh logging events")
    print("")
    print("!----------------TIME AND CLOCK SERVICES ---------------------------------")
    print("! if you have internet access use a NTP server to keep the clock accurate")
    print("! If you have multiple routers and switches, only have 1 device go directly to a internet")
    print("! NTP server The rest of the devices can use the internal device as a NTP server")
    print("")
    print("")
    print("clock timezone EST -5")
    print("clock summer-time EDT recurring")
    print("")
    print("! ntp3.cs.wisc.edu")
    print("tp server 128.105.37.11")
    print("! clock.psu.edu penn state U")
    print("tp server 128.118.25.3")
    print("! tick.jrc.us Jensen Research Corporation Oakland NJ")
    print("ntp server 67.128.71.65")
    print("! ntp1.kansas.net  KansasNet OnLine Services, Manhattan, KS")
    print("ntp server 199.240.130.1")
    print("! ntp-1.cso.uiuc.edu  - University of Illinois, Urbana-Champaign, IL")
    print("ntp server 130.126.24.24")
    print("! ntp1.sf-bay.org")
    print("ntp server 192.83.249.28")
    print("! clock1.unc.edu - University of North Carolina-Chapel Hill, Chapel Hill, NC")
    print("ntp server 152.2.21.1")
    print("! tick.usno.navy.mil  - http://tycho.usno.navy.mil/ntp.html")
    print("ntp server 192.5.41.40")
    print("! tock.usno.navy.mil")
    print("ntp server 192.5.41.41")
    print("")
    print("aaa new-model")
    print("aaa authentication login default local")
    print("")
    print("username corebts privilege 15 secret 4Support911")
    print("username customer privilege 15 secret customerpassword")
    print("")
    print("!------------------- BELOW ARE LINE AND TELENT COMMANDS TO USE Local AAA ------------------------------------------------")
    print("")
    print("line con 0")
    print("exec-timeout 30 0")
    print("privilege level 15")
    print("logging synchronous")
    print("")
    print("line aux 0")
    print("privilege level 15")
    print("logging synchronous")
    print("")
    print("line vty 0 15")
    print("exec-timeout 30 0")
    print("privilege level 15")
    print("logging synchronous")
    print("transport preferred none")
    print("")
    print("")
    print("")
    print("! ============================================================================================")
    print("! -------------------------------- END OF STANDARD COMMANDS FOR A TYPICAL BUILD --------------")
    print("! -------------------------------- EVERYTHING BELOW THIS IS OPTIONAL OR USED IN SPECIFIC CASES")
    print("! ============================================================================================")
    print("")
    print("")
    print("! ============================================================================================")
    print("! -------------------------------- External TACACS/RADIUS Server config ----------------------")
    print("! ============================================================================================")
    print("! below example uses a TACACS+ server, make sure that there is a way to authenticate when the TACACS")
    print("! server is unavailable and test it or you'll be locked out")
    print("!")
    print("aaa authentication login default group tacacs+ enable")
    print("aaa authentication login aaa-login group tacacs+ enable")
    print("aaa authentication login aaa-none none")
    print("aaa authorization exec aaa-auth group tacacs+ none")
    print("aaa authorization network default group tacacs+")
    print("aaa accounting exec default start-stop group tacacs+")
    print("aaa accounting commands 15 default start-stop group tacacs+")
    print("aaa accounting connection default start-stop group tacacs+")
    print("aaa accounting system default start-stop group tacacs+")
    print("")
    print(" ip tacacs source-interface (ethernet 0 or 0/1 etc...)")
    print(" tacacs-server host xxx.xxx.xxx.xx single-connection timeout 5 key TypeKeyHere")
    print("")
    print("!")
    print("! use the 'secret' keyword and not the 'password' keyword on local user accounts")
    print("username InacomUserName privilege 15 secret 0 PasswordGoesHere")
    print("!=======================================================================")
    print("Example-Radius server group - Traditional Method")
    print("")
    print("aaa group server radius RadiusServers1")
    print(" server-private 1.1.1.1 auth-port 1645 acct-port 1646 key secretphrase")
    print(" ip radius source-interface FastEthernet0/0.25")
    print("!=======================================================================")
    print("Example-Radius server group - New Method")
    print("")
    print("radius server RADIUS-SERVER-1")
    print("  address ipv4 1.1.1.1")
    print("  key secretphrase")
    print("aaa group server radius RADIUS-SERVER-1")
    print("  server name RADIUS-SERVER-1")
    print("")
    print("")
    print("")
    print("!========================================================")
    print("! Below example is using a radius server group first, then local database, then enable secret")
    print("aaa new-model")
    print("aaa group server radius RadiusServers1")
    print("server-private 1.1.1.1 auth-port 1645 acct-port 1646 key secretphrase")
    print("radius-server timeout 2")
    print("")
    print("! If the TACACS+ server is not reachable, the password prompt defined in the aaa authentication password-prompt command may be used.")
    print(" aaa authentication password-prompt **TACACS-DOWN-AUTHORIZED_USERS_ONLY**")
    print(" aaa authentication login aaa-login group RadiusServers1 local enable")
    print(" aaa authentication login aaa-none none")
    print(" aaa authorization exec aaa-auth group RadiusServers1 local none")
    print("")
    print("line con 0")
    print("login authentication aaa-none")
    print("")
    print("line aux 0")
    print("login authentication aaa-none")
    print("")
    print("line vty 0 15")
    print("exec-timeout 30 0")
    print("login authentication aaa-login")
    print("authorization exec aaa-auth")
    print("")
    print("! ============================================================================================")
    print("! -------------------------------- END External TACACS/RADIUS Server config ------------------")
    print("! ============================================================================================")
    print("")
    print("")
    print("")
    print("")
    print("!==============================================================================")
    print("")
    print("!------------------------STANDARD MANAGEMENT ACCESS TELNET & CONSOLE ------------------------------------")
    print("! Used when local AAA is not desired.  Use password command on the CON and VTY lines")
    print("!used to control who can telnet to the router.  dont allow telnet access from the internet! access list 66 permits the listed nets telnet access, remember that if the router is outside")
    print("! the PIX the source telnet addresses will be  NATted")
    print("! ip access-list standard management")
    print("! permit xxx.xxx.xxx.xxx yyy.yyy.yyy.yyy (source network with reverse mask that is allowed to telnet to router)")
    print("")
    print("! line con 0")
    print("! logging synchronous")
    print("")
    print("!line vty 0 4")
    print("! access-class management in *** use correct access list here***")
    print("! exec-timeout 30")
    print("! login")
    print("")
    print("! Core BTS Range if you want to allow from outside.  This range allows you to connect from Full VPN 199.48.156.0/22")
    print("")
    print("")
    print("!! IOS DHCP SERVER EXAMPLE")
    print("")
    print("ip dhcp excluded-address 10.200.5.0 10.200.5.200")
    print("ip dhcp database flash:dhcp.dat")
    print("ip dhcp ping packets 2")
    print("ip dhcp ping timeout 100")
    print("")
    print("!")
    print("ip dhcp pool VLAN55")
    print("network 10.200.5.0 255.255.255.0")
    print("default-router 10.200.5.1")
    print("dns-server 10.1.4.18 10.1.4.20")
    print("domain-name customer.com")
    print("netbios-node-type h-node")
    print("netbios-name-server 10.1.4.20 10.1.4.18")
    print("option 150 ip 1.1.1.1 2.2.2.2")
    print("lease 0 1 15")
    print("! the lease time duration is DAYS HOURS MINUTES")
    print("! the above is 0 DAYS 1 hour 15 minutes")
    print("")
    print("!=========TRACK INTERFACE EXAMPLE ====================")
    print("! used with HSRP")
    print("")
    print("track 100 rtr 123 reachability")
    print("")
    print("rtr 123")
    print("type echo protocol ipIcmpEcho 172.18.254.5 source-ipaddr 172.18.254.6")
    print("timeout 2000")
    print("threshold 40")
    print("frequency 3")
    print("rtr schedule 123 life forever start-time now")
    print("")
    print("interface Vlan1")
    print("description Denver Corporate Data Network")
    print("ip address 172.26.12.18 255.255.254.0")
    print("no ip redirects")
    print("standby 2 ip 172.26.12.1")
    print("standby 2 priority 140")
    print("standby 2 preempt")
    print("standby 2 authentication DATA")
    print("standby 2 track 100 decrement 30")
    print("")
    print("!==========================================================")
    print("")
    print("! make router be a time server")
    print("clock timezone EST -5")
    print("clock summer-time EDT recurring")
    print("clock calendar-valid")
    print("ntp master 1")
    print("")
    print("config t")
    print("int g0/0")
    print("ntp broadcast")
    print("ntp broadcast client")
    print("")
    print("")
    print("!==========================================================")
    print("! Setup AUX port for reverse telnet to console of another router, probably never used")
    print("line aux 0")
    print("location **Used to reverse telnet to Internet router console")
    print("login authentication aaa-none")
    print("modem InOut")
    print("no exec")
    print("transport input all")
    print("")
    print("! login note on aaa-none - This assumes you have AAA configured. this eliminates the authentication when doing")
    print("! the reverse telnet. - not required - assumes you have created 'aaa authentication login aaa-none none'")
    print("! speed defaults to 9600, no flowcontrol")
    print("")
    print("!==========================================================")
    print("")
    print("!==========================================================")
    print("!Creating a basic user menu")
    print("!This is intended to set up a basic 'read only' menu for a specific user")
    print("!You can set this up for the user to give you some basic commands without")
    print("!having to tell them to type such and such a command, because we all know")
    print("!how painful that can be.")
    print("")
    print("!This assumes a local user at privilege level 15 - even though the user is")
    print("!priv 15, they won't be able to make changes because the autocommand will run")
    print("!when they log inv")
    print("")
    print("!You can obviously modify the commands as needed")
    print("")
    print("")
    print("username USER autocommand menu READ_ONLY_MENU")
    print("menu READ_ONLY_MENU title ^")
    print("*******************************************************************************")
    print("                      Company Name Here - $(hostname)")
    print("                        YOU ARE IN A READ ONLY VIEW")
    print("*******************************************************************************")
    print("^")
    print("menu READ_ONLY_MENU single-space")
    print("menu READ_ONLY_MENU prompt ^ Please choose a command> ^")
    print("menu READ_ONLY_MENU text 1 Show running configuration (user and password info omitted)")
    print("menu READ_ONLY_MENU command 1 show run | exclude password|secret|READ_ONLY_MENU")
    print("menu READ_ONLY_MENU text 2 Show snmp-related information")
    print("menu READ_ONLY_MENU command 2 show run | include snmp")
    print("menu READ_ONLY_MENU text 3 Show interface f0/0 details")
    print("menu READ_ONLY_MENU command 3 show int f0/0")
    print("menu READ_ONLY_MENU text 4 Show interface f0/1 details")
    print("menu READ_ONLY_MENU command 4 show int f0/1")
    print("menu READ_ONLY_MENU text 5 Show the routing table")
    print("menu READ_ONLY_MENU command 5 show ip route")
    print("menu READ_ONLY_MENU text 6 exit")
    print("menu READ_ONLY_MENU command 6 exit")





















