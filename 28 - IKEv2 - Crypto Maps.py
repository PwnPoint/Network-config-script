from netmiko import ConnectHandler

router_num = input("How many routers would you like to configure: ")
router_num = int(router_num)

while router_num > 0:

    HOST = input("Enter the IP Address of Device to be Configured: ")
    user = input("Enter your SSH username: ")
    PASS = input("Enter your Password: ")

    ABC = {
        'device_type': 'cisco_ios',
        'host':   HOST,
        'username': user,
        'password': PASS
    }

    peer = input('Type the IP Address of remote peer:')
    print('\nIKEv2 Phase I Parameters\n')
    P1_hash =  input('Specify the Phase I Integrity - [MD5 | SHA]: ')
    P1_encryption =  input('Specify the Phase I Encryption - [DES | 3DES] :')
    P1_group =  input('Specify the Phase I DH Group: [1 | 2 | 5] : ')
    psk =  input('Specify the Pre-shared-Key : ')
    print('\nPhase II Parameters\n')
    P2_hash =  input('Specify the Phase II Hash - [MD5 | SHA]: ')
    P2_encryption =  input('Specify the Phase II Encryption - [DES | 3DES] :')
    print('\nCrypto ACL Networks\n')
    s_network =  input('Specify the source network: ')
    s_mask =  input('Specify the source wildcard mask: ')
    d_network =  input('Specify the Destination network: ')
    d_mask =  input('Specify the Destination wildcard mask: ')
    print('\nInterface\n')
    int_o =  input('Specify the outgoing interface: ')
    config_file = open('ikev2.txt', "w")
    config_file.write('crypto ikev2 proposal PROP1')
    config_file.write("\n")
    config_file.write(' Integrity ' + P1_hash)
    config_file.write("\n")
    config_file.write(' encryption ' + P1_encryption)
    config_file.write("\n")
    config_file.write(' group ' + P1_group)
    config_file.write("\n")
    config_file.write('!\ncrypto ikev2 policy POL1\n')
    config_file.write(' proposal PROP1\n')
    config_file.write('!\ncrypto ikev2 keyring KR1\n')
    config_file.write(' peer REMOTE\n')
    config_file.write('  address ' + peer + '\n')
    config_file.write('  pre-shared-key ' + psk + '\n')
    config_file.write('!\ncrypto ikev2 profile IKEv2-PROF\n')
    config_file.write(' match identity remote address ' + peer + '\n')
    config_file.write(' authentication local pre-share\n')
    config_file.write(' authentication remote pre-share\n')
    config_file.write(' Keyring local KR1\n')
    config_file.write('!\ncrypto ipsec transform-set TSET esp-' + P2_hash + '-hmac esp-' +P2_encryption + '\n')
    config_file.write('!\nip access-list extended CRYPTO-ACL\n')
    config_file.write(' permit ip ' + s_network + ' ' + s_mask + ' ' + d_network + ' ' + d_mask + '\n')
    config_file.write('!\ncrypto map C_MAP 10 ipsec-isakmp\n')
    config_file.write(' set peer ' +  peer + '\n')
    config_file.write(' set ikev2-profile IKEv2-PROF\n')
    config_file.write(' set transform-set TSET\n')
    config_file.write(' match address CRYPTO-ACL\n')
    config_file.write('!\nInterface ' +  int_o + '\n')
    config_file.write(' crypto map C_MAP\n')
    config_file.close()

    MYSSH = ConnectHandler(**ABC)

    cmdfile = 'ikev2.txt'
    output=MYSSH.send_config_from_file(cmdfile)
    print(output)
    print('IPSec Configured')
    MYSSH.disconnect()
    router_num -=1

input('Press Enter to Finish')
