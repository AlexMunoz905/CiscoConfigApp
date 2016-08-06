service tcp-keepalives-in
service tcp-keepalives-out
service timestamps debug datetime msec localtime show-timezone                    
service timestamps log datetime msec localtime show-timezone     
service password-encryption
service sequence-numbers  
exception crashinfo maximum files 2
! Speed up large configurations when accessed
parser config cache interface
parser config partition
warm-reboot count 10 uptime 5
exception memory ignore overflow io
exception memory ignore overflow processor
!
!
no service tcp-small-servers
no service udp-small-servers  
no service pad
no ip finger
no service finger
no ip http server
no ip http secure-server
no service config
!
ip cef
ip classless
ip subnet-zero
no ip source-route
!
!
no ip domain-lookup
ip tcp synwait-time 5
!
logging buffered 256000 debugging
no logging console
logging monitor critical
logging trap debugging
!
archive
 log config
  logging enable
  logging size 1000
  notify syslog
  hidekeys
!
archive 
  path flash:BackupConfig
  maximum 7
  write-memory
!
no enable password

enable secret -StringHere-

login on-failure log
login on-success log

no snmp-server community public RO
no snmp-server community private RW
snmp-server ifindex persist

no banner motd
banner motd ^
**********************************************************************
WARNING: This system is for the use of authorized clients only.
Individuals using the computer network system without authorization,
or in excess of their authorization, are subject to having all their
activity on this computer network system monitored and recorded by
system personnel.  To protect the computer network system from
unauthorized use and to ensure the computer network systems is
functioning properly, system administrators monitor this system.
Anyone using this computer network system expressly consents to such
monitoring and is advised that if such monitoring reveals possible
conduct of criminal activity, system personnel may provide the
evidence of such activity to law enforcement officers          
Access is restricted to authorized users only. Unauthorized access is
a violation of state and federal, civil and criminal laws
**********************************************************************
^


banner exec ^
**********************************************************************
                        Company Name
                        HOST: $(hostname)
                        Configured for Data and Voice Use
**********************************************************************
^

crypto key generate rsa general-keys modulus 2048
ip ssh time-out 29
ip ssh authentication-retries 2
ip ssh version 2
ip ssh logging events

!----------------TIME AND CLOCK SERVICES ---------------------------------
! if you have internet access use a NTP server to keep the clock accurate
! If you have multiple routers and switches, only have 1 device go directly to a internet 
! NTP server The rest of the devices can use the internal device as a NTP server


clock timezone EST -5
clock summer-time EDT recurring

! ntp3.cs.wisc.edu 
ntp server 128.105.37.11 
! clock.psu.edu penn state U
ntp server 128.118.25.3 
! tick.jrc.us Jensen Research Corporation Oakland NJ 
ntp server 67.128.71.65 
! ntp1.kansas.net  KansasNet OnLine Services, Manhattan, KS 
ntp server 199.240.130.1 
! ntp-1.cso.uiuc.edu  - University of Illinois, Urbana-Champaign, IL
ntp server 130.126.24.24 
! ntp1.sf-bay.org 
ntp server 192.83.249.28 
! clock1.unc.edu - University of North Carolina-Chapel Hill, Chapel Hill, NC 
ntp server 152.2.21.1 
! tick.usno.navy.mil  - http://tycho.usno.navy.mil/ntp.html
ntp server 192.5.41.40
! tock.usno.navy.mil 
ntp server 192.5.41.41

aaa new-model
aaa authentication login default local
 
username corebts privilege 15 secret 4Support911
username customer privilege 15 secret customerpassword

!------------------- BELOW ARE LINE AND TELENT COMMANDS TO USE Local AAA ------------------------------------------------

line con 0
exec-timeout 30 0
 privilege level 15
 logging synchronous
  
line aux 0 
 privilege level 15
 logging synchronous

line vty 0 15
exec-timeout 30 0
 privilege level 15
 logging synchronous
 transport preferred none



! ============================================================================================
! -------------------------------- END OF STANDARD COMMANDS FOR A TYPICAL BUILD --------------
! -------------------------------- EVERYTHING BELOW THIS IS OPTIONAL OR USED IN SPECIFIC CASES
! ============================================================================================


! ============================================================================================
! -------------------------------- External TACACS/RADIUS Server config ----------------------
! ============================================================================================
! below example uses a TACACS+ server, make sure that there is a way to authenticate when the TACACS 
! server is unavailable and test it or you'll be locked out
! 
aaa authentication login default group tacacs+ enable
aaa authentication login aaa-login group tacacs+ enable
aaa authentication login aaa-none none
aaa authorization exec aaa-auth group tacacs+ none 
aaa authorization network default group tacacs+ 
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 15 default start-stop group tacacs+
aaa accounting connection default start-stop group tacacs+
aaa accounting system default start-stop group tacacs+

! ip tacacs source-interface (ethernet 0 or 0/1 etc...)
! tacacs-server host xxx.xxx.xxx.xx single-connection timeout 5 key TypeKeyHere

!
! use the "secret" keyword and not the "password" keyword on local user accounts
username InacomUserName privilege 15 secret 0 PasswordGoesHere
!=======================================================================
Example-Radius server group - Traditional Method

aaa group server radius RadiusServers1
 server-private 1.1.1.1 auth-port 1645 acct-port 1646 key secretphrase 
 ip radius source-interface FastEthernet0/0.25
!=======================================================================
Example-Radius server group - New Method

radius server RADIUS-SERVER-1
  address ipv4 1.1.1.1
  key secretphrase
aaa group server radius RADIUS-SERVER-1
  server name RADIUS-SERVER-1



!========================================================
! Below example is using a radius server group first, then local database, then enable secret
aaa new-model
aaa group server radius RadiusServers1
 server-private 1.1.1.1 auth-port 1645 acct-port 1646 key secretphrase 
radius-server timeout 2 

! If the TACACS+ server is not reachable, the password prompt defined in the aaa authentication password-prompt command may be used. 
 aaa authentication password-prompt **TACACS-DOWN-AUTHORIZED_USERS_ONLY**
 aaa authentication login aaa-login group RadiusServers1 local enable
 aaa authentication login aaa-none none
 aaa authorization exec aaa-auth group RadiusServers1 local none
 
 line con 0
 login authentication aaa-none
 
line aux 0 
 login authentication aaa-none 

line vty 0 15
exec-timeout 30 0
login authentication aaa-login
authorization exec aaa-auth

! ============================================================================================
! -------------------------------- END External TACACS/RADIUS Server config ------------------
! ============================================================================================




!==============================================================================

!------------------------STANDARD MANAGEMENT ACCESS TELNET & CONSOLE ------------------------------------
! Used when local AAA is not desired.  Use password command on the CON and VTY lines
!used to control who can telnet to the router.  dont allow telnet access from the internet! access list 66 permits the listed nets telnet access, remember that if the router is outside
! the PIX the source telnet addresses will be  NATted
! ip access-list standard management
! permit xxx.xxx.xxx.xxx yyy.yyy.yyy.yyy (source network with reverse mask that is allowed to telnet to router)

! line con 0
! logging synchronous

!line vty 0 4
! access-class management in *** use correct access list here***
! exec-timeout 30
! login

! Core BTS Range if you want to allow from outside.  This range allows you to connect from Full VPN 199.48.156.0/22


!! IOS DHCP SERVER EXAMPLE

ip dhcp excluded-address 10.200.5.0 10.200.5.200
ip dhcp database flash:dhcp.dat
ip dhcp ping packets 2
ip dhcp ping timeout 100

!
ip dhcp pool VLAN55
   network 10.200.5.0 255.255.255.0
   default-router 10.200.5.1 
   dns-server 10.1.4.18 10.1.4.20 
   domain-name customer.com
   netbios-node-type h-node
   netbios-name-server 10.1.4.20 10.1.4.18 
   option 150 ip 1.1.1.1 2.2.2.2 
   lease 0 1 15
   ! the lease time duration is DAYS HOURS MINUTES
   ! the above is 0 DAYS 1 hour 15 minutes
   
!=========TRACK INTERFACE EXAMPLE ====================
! used with HSRP

track 100 rtr 123 reachability

rtr 123   
 type echo protocol ipIcmpEcho 172.18.254.5 source-ipaddr 172.18.254.6
 timeout 2000
 threshold 40
 frequency 3
rtr schedule 123 life forever start-time now

interface Vlan1
 description Denver Corporate Data Network
 ip address 172.26.12.18 255.255.254.0
 no ip redirects
 standby 2 ip 172.26.12.1
 standby 2 priority 140
 standby 2 preempt
 standby 2 authentication DATA
 standby 2 track 100 decrement 30
 
!==========================================================

! make router be a time server
clock timezone EST -5
clock summer-time EDT recurring
clock calendar-valid
ntp master 1

config t
int g0/0
ntp broadcast
ntp broadcast client


!==========================================================
! Setup AUX port for reverse telnet to console of another router, probably never used
line aux 0
 location **Used to reverse telnet to Internet router console
 login authentication aaa-none
 modem InOut
 no exec
 transport input all

! login note on aaa-none - This assumes you have AAA configured. this eliminates the authentication when doing
! the reverse telnet. - not required - assumes you have created "aaa authentication login aaa-none none"
! speed defaults to 9600, no flowcontrol

!==========================================================

!==========================================================
!Creating a basic user menu
!This is intended to set up a basic "read only" menu for a specific user
!You can set this up for the user to give you some basic commands without
!having to tell them to type such and such a command, because we all know 
!how painful that can be.

!This assumes a local user at privilege level 15 - even though the user is
!priv 15, they won't be able to make changes because the autocommand will run
!when they log in

!You can obviously modify the commands as needed


username USER autocommand menu READ_ONLY_MENU
menu READ_ONLY_MENU title ^
*******************************************************************************
                      Company Name Here - $(hostname)
                        YOU ARE IN A READ ONLY VIEW
*******************************************************************************
^
menu READ_ONLY_MENU single-space
menu READ_ONLY_MENU prompt ^ Please choose a command> ^
menu READ_ONLY_MENU text 1 Show running configuration (user and password info omitted)
menu READ_ONLY_MENU command 1 show run | exclude password|secret|READ_ONLY_MENU
menu READ_ONLY_MENU text 2 Show snmp-related information
menu READ_ONLY_MENU command 2 show run | include snmp
menu READ_ONLY_MENU text 3 Show interface f0/0 details
menu READ_ONLY_MENU command 3 show int f0/0
menu READ_ONLY_MENU text 4 Show interface f0/1 details
menu READ_ONLY_MENU command 4 show int f0/1
menu READ_ONLY_MENU text 5 Show the routing table
menu READ_ONLY_MENU command 5 show ip route
menu READ_ONLY_MENU text 6 exit
menu READ_ONLY_MENU command 6 exit





















