# vlan_deploy.py
import yaml
from netmiko import ConnectHandler

vlan_id = "100"
vlan_name = "Automation_VLAN"

with open("inventory.yml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    print(f"\n🔧 Creating VLAN on {dev['host']}")
    try:
        conn = ConnectHandler(**dev)
        conn.enable()
        config = [f"vlan {vlan_id}", f"name {vlan_name}"]
        conn.send_config_set(config)
        print(f"✅ VLAN {vlan_id} created")
        conn.disconnect()
    except Exception as e:
        print(f"❌ {dev['host']} failed: {e}")
