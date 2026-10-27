import yaml
import logging
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler

logging.basicConfig(
    filename="bgp_push.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load inventory
def load_inventory():
    with open("inventory.yml") as f:
        return yaml.safe_load(f)["devices"]

# Build BGP config dynamically
def build_bgp_config(device, all_devices):
    commands = []
    commands.append(f"router bgp {device['asn']}")

    for peer in all_devices:
        if peer["host"] != device["host"]:
            commands.append(
                f"neighbor {peer['host']} remote-as {peer['asn']}"
            )

    return commands

# Push config to device
def configure_device(device, all_devices):
    host = device["host"]

    try:
        print(f"Connecting to {host}")

        # Build Netmiko connection dictionary ONLY
        connection_params = {
            "device_type": device["device_type"],
            "host": device["host"],
            "username": device["username"],
            "password": device["password"],
            "secret": device["secret"],
        }

        conn = ConnectHandler(**connection_params)
        conn.enable()

        # Backup before change
        backup = conn.send_command("show running-config")
        with open(f"backup_{host}.txt", "w") as f:
            f.write(backup)

        logging.info(f"{host} - Backup completed")

        # Build config
        commands = build_bgp_config(device, all_devices)

        # Push BGP config
        output = conn.send_config_set(commands)
        print(f"{host} config pushed")

        # Save config
        conn.send_command("write memory")

        # Verification
        verify = conn.send_command("show ip bgp summary")
        print(f"\n{host} BGP Summary:\n{verify}\n")

        conn.disconnect()
        print(f"{host} completed ✅\n")

    except Exception as e:
        logging.error(f"{host} - {str(e)}")
        print(f"{host} failed ❌")

# Main
def main():
    devices = load_inventory()

    with ThreadPoolExecutor(max_workers=4) as executor:
        for device in devices:
            executor.submit(configure_device, device, devices)

    print("BGP Deployment Completed 🚀")

if __name__ == "__main__":
    main()