from netmiko import ConnectHandler

# Router details
router = {
    "device_type": "cisco_ios",
    "host": "192.168.12.131",
    "username": "admin",
    "password": "cisco123",
    "secret": "cisco123",
}

# BGP states considered "down"
down_states = ["Idle", "Active", "Connect"]

try:
    # Connect to the router
    connection = ConnectHandler(**router)
    connection.enable()

    # Run BGP summary command
    bgp_output = connection.send_command("show ip bgp summary")

    print("\n📋 Full BGP Summary Output:\n")
    print(bgp_output)

    print("\n🔍 BGP Neighbors which are Down:\n")

    # Skip lines until we find the header
    lines = bgp_output.strip().splitlines()
    print(lines)
    for index, line in enumerate(lines):
        if line.strip().startswith("Neighbor"):
            data_lines = lines[index + 1:]  # Get all data lines after header
            break
    else:
        print("No BGP summary data found.")
        data_lines = []

    for line in data_lines:
        if not line.strip():
            continue  # Skip empty lines

        fields = line.split()
        print(fields)
        if len(fields) < 9:
            continue  # Not a valid BGP neighbor line

        neighbor_ip = fields[0]
        last_field = fields[-1]
        second_last = fields[-2]

        print(last_field)

        # Check if state is a string (like "Idle", "Active", "Connect") instead of number
        if last_field in down_states:
            print(f"Neighbor {neighbor_ip} is in state: {last_field}")
        elif not last_field.isdigit() and second_last in down_states:
            print(f"Neighbor {neighbor_ip} is in state: {second_last}")

    
except Exception as e:
    print(f"❌ Error: {e}")

finally:
    try:
        connection.disconnect()
    except:
        pass
