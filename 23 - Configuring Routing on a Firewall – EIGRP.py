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

eigrpas = input('EIGRP AS #: ')
routereigrp = 'router eigrp ' + eigrpas
network_num = input('How many networks would you like to enable in EIGRP: ')
network_num = int(network_num)
while network_num > 0:
    network = input('Please specify the network to enable: ')
    S_Mask = input('Please specify the Subnet Mask for the Network: ')
    network_cmd = 'network ' + network + ' ' + S_Mask
    config_commands = [routereigrp, network_cmd]
    output = myssh.send_config_set(config_commands)
    print(output)
    network_num -=1
print('-'*79)

input("Press ENTER to finish")
