from telnetlib import Telnet

myinterface = input('What Interface would you like to configure [E0/0,Loopback200 etc]:')
Ipaddr = input('Specify the IP Address : ')
SMask = input('Specify the Subnet mask : ')

my_var = Telnet('172.25.1.1')
my_var.write(b'cisco\n')
my_var.write(b'cisco\n')
my_var.write(b'config t\n')

int_cmd='Interface ' + myinterface + '\n'
ipaddr_cmd ='ip address ' + Ipaddr + ' ' + SMask + '\n'

my_var.write(int_cmd.encode('ascii'))
my_var.write(ipaddr_cmd.encode('ascii'))
my_var.write(b'no shut\n')
my_var.write(b'end\n')
my_var.write(b'sh ip int brief\n')
my_var.write(b'exit\n')
print (my_var.read_all().decode('ascii'))
input('Press ENTER to Continue')
