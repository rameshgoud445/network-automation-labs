import yaml
from netmiko import ConnectHandler

# Load YAML file
with open("bgp_multiple.yml") as file:
    data = yaml.safe_load(file)

routers = data["routers"]
print(routers)


def configure_router(router, details):
    try:
        device = {
            "device_type": details["device_type"],
            "host": details["host"],
            "username": details["username"],
            "password": details["password"],
        }

        print(f"\nConnecting to {router}")

        connection = ConnectHandler(**device)

        config_commands = []

        # Interface Configuration
        for interface in details["interfaces"]:
            config_commands.append(f"interface {interface['name']}")
            config_commands.append(
                f"ip address {interface['ip']} {interface['mask']}"
            )
            config_commands.append("no shutdown")

        print("Config commands:", config_commands)

        # BGP Configuration
        config_commands.append(f"router bgp {details['asn']}")

        for neighbor in details["neighbors"]:
            config_commands.append(
                f"neighbor {neighbor['ip']} remote-as {neighbor['remote_as']}"
            )

        # Push config
        output = connection.send_config_set(config_commands)

        print(f"\n{router} Configuration Output:")
        print(output)

        # Verify BGP
        print(f"\nChecking BGP Neighborship on {router}")
        bgp_output = connection.send_command("show ip bgp summary")

        print(f"\n{router} BGP Summary:")
        print(bgp_output)

        connection.disconnect()

        print(f"{router} Completed Successfully ✅")

    except Exception as e:
        print(f"{router} Failed ❌")
        print(f"Error: {e}")


def main():
    # Loop one by one (no threading)
    for router, details in routers.items():
        configure_router(router, details)

    print("\nAutomation Completed Successfully 🚀")


if __name__ == "__main__":
    main().. please give good name