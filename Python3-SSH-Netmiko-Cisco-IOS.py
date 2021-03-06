# Python3 SSH test using Netmiko

from netmiko import ConnectHandler

LabSW3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.2.238',
    'username': 'dave',
    'password': 'MyPass',
}

LabSW4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.2.239',
    'username': 'dave',
    'password': 'MyPass',
}

LabSW5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.2.240',
    'username': 'dave',
    'password': 'MyPass',
}


all_devices = [LabSW3, LabSW4, LabSW5]
# all_devices = [LabSW5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)

    # Show model number of each switch
    output = net_connect.send_command('show version | include Model number')
    print(output)
    
    # Add description to first 2 loopback interfaces
    for n in range (1,3):
        config_commands = ['interface loopback ' + str(n), 'description My loopback interface ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
