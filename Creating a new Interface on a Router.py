from telnetlib import Telnet

my_var = Telnet('172.25.1.1')
my_var.write(b'cisco\n')
my_var.write(b'cisco\n')
my_var.write(b'config t\n')
my_var.write(b'Interface Loopback55\n')
my_var.write(b'ip address 55.5.5.5 255.255.255.0\n')
my_var.write(b'end\n')
my_var.write(b'sh ip int brief\n')
my_var.write(b'exit\n')
print (my_var.read_all().decode('ascii'))
input('Press ENTER to Continue')
