from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.12.130",
    "username": "admin",
    "password": "cisco123",
}

connection = ConnectHandler(**device)

config_command = [
    "interface loopback 5",
    "ip address 5.5.5.5 255.255.255.255",
    "description Counfigured_by_netmiko"
]

output = connection.send_config_set(config_command)
output1 = connection.send_command("show ip int br")
print(output1)
print(output)

connection.disconnect()
