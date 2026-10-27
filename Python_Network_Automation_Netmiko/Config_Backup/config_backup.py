# backup_configs.py
import yaml
from netmiko import ConnectHandler
from datetime import datetime

with open("inventory.yml") as f:
    devices = yaml.safe_load(f)["devices"]

for dev in devices:
    try:
        conn = ConnectHandler(**dev)
        conn.enable()
        output = conn.send_command("show running-config")
        
        filename = f"backups/{dev['host']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.cfg"
        with open(filename, "w") as f:
            f.write(output)
        print(f"✅ Backup saved for {dev['host']} at {filename}")
        conn.disconnect()
    except Exception as e:
        print(f"❌ {dev['host']} failed: {e}")