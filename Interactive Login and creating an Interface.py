from telnetlib import Telnet

HOST = input('Specify the Host IP : ')
USER = input('Specify the Username: ')
PASS = input('Specify the Password: ')

Interface = input('What Interface would you like to configure : ')
Ipaddr = input('Specify the IP Address : ')
SMask = input('Specify the Subnet mask : ')

my_var = Telnet(HOST)
my_var.write(USER.encode('ascii') + b'\n')
my_var.write(PASS.encode('ascii') + b'\n')

int_cmd = 'Interface ' + Interface + '\n'
ipaddr_cmd = 'IP Address ' + Ipaddr + ' ' + SMask + '\n'
my_var.write(b'config t\n')
my_var.write(int_cmd.encode('ascii'))
my_var.write(ipaddr_cmd.encode('ascii'))
my_var.write(b'end\n')
my_var.write(b'sh ip int brief\n')
my_var.write(b'exit\n')
print (my_var.read_all().decode('ascii'))
input('Press Enter to Continue')
