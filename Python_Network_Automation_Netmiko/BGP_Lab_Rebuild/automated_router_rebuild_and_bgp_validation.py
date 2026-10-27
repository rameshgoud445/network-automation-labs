from netmiko import ConnectHandler
import time

username = "admin"
password = "cisco123"
secret = "cisco123"

routers = {
    "R1": {
        "host": "192.168.12.130",
        "as": 100,
        "config": [
            "hostname R1",
            "interface loopback0",
            "ip address 1.1.1.1 255.255.255.255",
            "no shutdown",
            "interface g1/0",
            "ip address 192.168.21.1 255.255.255.0",
            "no shutdown",
            "router bgp 100",
            "neighbor 192.168.21.2 remote-as 200",
            "network 1.1.1.1 mask 255.255.255.255"
        ]
    },

    "R2": {
        "host": "192.168.12.131",
        "as": 200,
        "config": [
            "hostname R2",
            "interface loopback0",
            "ip address 2.2.2.2 255.255.255.255",
            "no shutdown",
            "interface g1/0",
            "ip address 192.168.21.2 255.255.255.0",
            "no shutdown",
            "interface g2/0",
            "ip address 192.168.23.2 255.255.255.0",
            "no shutdown",
            "router bgp 200",
            "neighbor 192.168.21.1 remote-as 100",
            "neighbor 192.168.23.3 remote-as 300",
            "network 2.2.2.2 mask 255.255.255.255"
        ]
    },

    "R3": {
        "host": "192.168.12.132",
        "as": 300,
        "config": [
            "hostname R3",
            "interface loopback0",
            "ip address 3.3.3.3 255.255.255.255",
            "no shutdown",
            "interface g2/0",
            "ip address 192.168.23.3 255.255.255.0",
            "no shutdown",
            "interface g1/0",
            "ip address 192.168.34.3 255.255.255.0",
            "no shutdown",
            "router bgp 300",
            "neighbor 192.168.23.2 remote-as 200",
            "neighbor 192.168.34.4 remote-as 400",
            "network 3.3.3.3 mask 255.255.255.255"
        ]
    },

    "R4": {
        "host": "192.168.12.133",
        "as": 400,
        "config": [
            "hostname R4",
            "interface loopback0",
            "ip address 4.4.4.4 255.255.255.255",
            "no shutdown",
            "interface g1/0",
            "ip address 192.168.34.4 255.255.255.0",
            "no shutdown",
            "router bgp 400",
            "neighbor 192.168.34.3 remote-as 300",
            "network 4.4.4.4 mask 255.255.255.255"
        ]
    }
}

bgp_down = []

for name, router in routers.items():

    device = {
        "device_type": "cisco_ios",
        "host": router["host"],
        "username": username,
        "password": password,
        "secret": secret
    }

    print(f"\nConnecting to {name}")

    try:

        conn = ConnectHandler(**device)
        conn.enable()

        print(f"Erasing configuration on {name}")

        output = conn.send_command_timing("write erase")
        if "confirm" in output:
           output += conn.send_command_timing("\n")

        output += conn.send_command_timing("reload")
        if "confirm" in output:
            output += conn.send_command_timing("\n")

        print(output)
        conn.send_command("\n")

        print("Waiting for device reload...")
        time.sleep(120)

        conn.disconnect()

        conn = ConnectHandler(**device)
        conn.enable()

        print(f"Pushing configuration to {name}")

        output = conn.send_config_set(router["config"])
        print(output)

        conn.send_command("write memory")

        print(f"Checking BGP state on {name}")

        bgp = conn.send_command("show ip bgp summary")

        if "Estab" not in bgp:
            bgp_down.append(name)

        conn.disconnect()

    except Exception as e:
        print(f"Error on {name} : {e}")

print("\n===============================")
print("POST CHECK RESULT")
print("===============================")

if bgp_down:
    print("BGP NOT Established on routers:")
    for r in bgp_down:
        print(r)
else:
    print("All BGP Sessions Established Successfully")