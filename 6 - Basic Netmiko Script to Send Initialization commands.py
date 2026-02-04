from netmiko import ConnectHandler

ABC = {
    'device_type': 'cisco_ios',
    'host':   '172.25.1.1',
    'username': 'cisco',
    'password': 'cisco'
}
myssh = ConnectHandler(**ABC)

config_commands = [ 'banner motd #Authorized KBITS.LIVE Users Only#',
                    'no ip domain-lookup',
                    'line con 0',
                    ' logg sync'
                    ]
myssh.send_config_set(config_commands)
output1 = myssh.send_command('sh runn | inc banner')
output2 = myssh.send_command('show run | sec line')
print(output1)
print(output2)
input('Press Enter to Continue')
