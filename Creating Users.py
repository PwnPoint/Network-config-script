from telnetlib import Telnet

HOST = input('Specify the Host IP : ')
USER = input('Specify the Username: ')
PASS = input('Specify the Password: ')

num_users = input('How many users would you like to create: ')
num_users = int(num_users)

my_var = Telnet(HOST)
my_var.write(USER.encode('ascii') + b'\n')
my_var.write(PASS.encode('ascii') + b'\n')
my_var.write(b'config t\n')

while (num_users > 0):
    username = input('Specify the Username to be created : ')
    userpass = input('Specify the Password: ')
    userpriv = input('Specify the exec level: ')

    my_var.write(b'Username ' + username.encode('ascii') + b' privilege ' + userpriv.encode('ascii') + b' password ' + userpass.encode('ascii') + b'\n')
    num_users -=1



my_var.write(b'end\n')
my_var.write(b'sh run | inc username\n')
my_var.write(b'exit\n')
print (my_var.read_all().decode('ascii'))
input('Press Enter to Continue')
