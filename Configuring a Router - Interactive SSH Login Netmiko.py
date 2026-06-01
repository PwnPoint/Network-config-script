from netmiko import ConnectHandler

HOST = input("Enter IP Address of the Device: ")
USER = input("Enter your SSH username: ")
PASS = input("Enter your SSH Password: ")

ABC = {
    'device_type': 'cisco_ios',
    'host':   HOST,
    'username': USER,
    'password': PASS
}
myssh = ConnectHandler(**ABC)

config_commands = [ 'Interface loopback 66',
                    'IP Address 160.1.1.1 255.255.255.0',
                    'no shut']

myssh.send_config_set(config_commands)
output = myssh.send_command('show ip int brief')
print(output)
input("Press ENTER to finish")
