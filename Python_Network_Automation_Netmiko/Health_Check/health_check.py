# health_check.py
import yaml
from netmiko import ConnectHandler

commands = {
    "CPU": "show processes cpu sorted | include one minute",
    "Memory": "show processes memory | include Processor",
    "Interfaces": "show ip int brief | exclude unassigned",
    "BGP": "show ip bgp summary",
    "OSPF": "show ip ospf neighbor",
}

with open("inventory.yml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    print(f"\n📊 Health Check for {dev['host']}")
    try:
        conn = ConnectHandler(**dev)
        conn.enable()
        for title, cmd in commands.items():
            print(f"\n--- {title} ---")
            print(conn.send_command(cmd))
        conn.disconnect()
    except Exception as e:
        print(f"❌ {dev['host']} failed: {e}")
