# pre_post_checks.py
import yaml
from netmiko import ConnectHandler

check_cmds = ["ping 8.8.8.8", "show ip route", "show ip bgp summary"]

def run_checks(conn, phase):
    print(f"\n--- {phase} Checks ---")
    for cmd in check_cmds:
        print(f"\n$ {cmd}")
        print(conn.send_command(cmd))

with open("inventory.yml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    conn = ConnectHandler(**dev)
    conn.enable()
    run_checks(conn, "Pre-Change")

    # 🔧 Example change (adjust as needed)
    conn.send_config_set(["interface loopback10", "ip address 10.10.10.1 255.255.255.255"])

    run_checks(conn, "Post-Change")
    conn.disconnect()
