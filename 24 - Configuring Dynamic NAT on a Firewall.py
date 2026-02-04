from netmiko import ConnectHandler

hostip = input('ASA Firewall IP: ')
USER = input('SSH Username: ')
PASS = input('SSH Password: ')
ASA = {
        'device_type': 'cisco_asa',
        'ip': hostip,
        'username': USER,
        'password': PASS
        }

myssh = ConnectHandler(**ASA)

print('\nPool Information - Range\n')
print('-' * 50)

Pool_name = input('Pool Name: ')
Pool_Start = input('Client Pool Start Address: ')
Pool_End = input('Client Pool End Address: ')

print('\nNAT Information\n')
print('-' * 50)
Local_subnet = input ('Specify the Local Subnet along with Mask [10.11.11.0 255.255.255.0]: ')
Local_interface = input ('Local Interface: ')
External_interface = input ('External Interface: ')

Pool_object = 'Object network ' + Pool_name
Pool_cmd = 'range ' + Pool_Start + ' ' + Pool_End

Local_object = 'Object network LOCAL_SUBNET'
subnet_cmd = 'subnet ' + Local_subnet
nat_cmd = 'nat (' + Local_interface + ',' + External_interface + ') dynamic ' + Pool_name

config_commands = [Pool_object, Pool_cmd,
                   Local_object, subnet_cmd, nat_cmd]
output = myssh.send_config_set(config_commands)
print(output)

print('-'*79)

input("Press ENTER to finish")

