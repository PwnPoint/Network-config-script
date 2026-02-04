from netmiko import ConnectHandler

hostip = input('ASA Firewall IP: ')
USER = input('SSH Username: ')
PASS = input('Password: ')

ASA = {
        'device_type': 'cisco_asa',
        'ip': hostip,
        'username': USER,
        'password': PASS
        }

myssh = ConnectHandler(**ASA)

Interface_num = input('How many Interfaces would you like to configure: ')
Interface_num = int(Interface_num)
while Interface_num > 0:
    Interface_ID = input('Please specify the Interface to be configured: [E0, gig0/0 etc]: ')
    Interface_IP = input('IP Address: ')
    S_Mask = input('Subnet Mask: ')
    Interface_cmd = 'Interface ' + Interface_ID
    IP_Address_cmd = 'IP Address ' + Interface_IP + ' ' + S_Mask

    Nameif = input('Interface Name: ')
    Nameif_cmd = 'Nameif ' + Nameif

    Sec_Level = input('Security Level: ')
    Sec_level_cmd = 'Security-Level ' + Sec_Level

    config_commands = [Interface_cmd, IP_Address_cmd, Nameif_cmd, Sec_level_cmd, 'no shut']

    output = myssh.send_config_set(config_commands)
    print(output)
    Interface_num -=1

Def_route = input('Would you like to configure a default route [Y/N]: ')
if Def_route.lower() == 'y':
    next_hop = input('Please specify the Default Gateway Addres: ')
    def_route_int = input('Outgoing Interface: ')
    Def_route_cmd = 'route ' + def_route_int +   ' 0 0 ' + next_hop

    config_commands = [Def_route_cmd]

    output = myssh.send_config_set(config_commands)
    print(output)
print('-'*79)
output = myssh.send_command('sh int ip brief')
print(output)

input("Press ENTER to finish")
