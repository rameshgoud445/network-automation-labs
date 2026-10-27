# compliance_check.py
import yaml
from netmiko import ConnectHandler

rules = {
    "aaa": "aaa new-model",
    "ssh": "transport input ssh",
    "banner": "banner motd",
    "snmp": "snmp-server community"
}

with open("inventory.yml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    print(f"\n🔍 Compliance Check: {dev['host']}")
    try:
        conn = ConnectHandler(**dev)
        conn.enable()
        run_cfg = conn.send_command("show running-config")
        for name, rule in rules.items():
            if rule in run_cfg:
                print(f"✅ {name} present")
            else:
                print(f"❌ {name} missing")
        conn.disconnect()
    except Exception as e:
        print(f"❌ Error on {dev['host']}: {e}")
