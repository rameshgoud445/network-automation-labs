import yaml
import logging
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

logging.basicConfig(
    filename="health_check.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

with open("inventory.yml") as file:
    devices = yaml.safe_load(file)["devices"]
    print("devices are.....................",devices)

for device in devices:
    host = device["host"]
    print(f"\nConnecting to {host}")

    try:
        connection = ConnectHandler(**device)
        connection.enable()

        ospf_output = connection.send_command("show ip ospf neighbor")
        print(ospf_output)
        if "FULL" in ospf_output:
            print("✅ OSPF OK")
            logging.info(f"{host} - OSPF OK")
        else:
            print("❌ OSPF ISSUE")
            logging.warning(f"{host} - OSPF ISSUE")

        bgp_output = connection.send_command("show ip bgp summary")
        print(bgp_output)
        if "Establ" in bgp_output:
            print("✅ BGP OK")
            logging.info(f"{host} - BGP OK")
        else:
            print("❌ BGP DOWN")
            logging.warning(f"{host} - BGP DOWN")

        connection.disconnect()

    except NetmikoTimeoutException:
        print("❌ Device not reachable")
        logging.error(f"{host} - Timeout")

    except NetmikoAuthenticationException:
        print("❌ Authentication failed")
        logging.error(f"{host} - Authentication failed")

    except Exception as e:
        print("❌ Unexpected error:", e)
        logging.error(f"{host} - Unexpected error {e}")

print("\nHealth check completed 🚀")