from netmiko import ConnectHandler

# Define router details
router = {
    "device_type": "cisco_ios",
    "host": "192.168.12.131",  # Router IP
    "username": "admin",        # SSH Username
    "password": "cisco123",      # SSH Password
    "secret": "cisco123",        # Enable Password
}

try:
    # Establish SSH connection
    connection = ConnectHandler(**router)
    
    # Enter enable mode
    connection.enable()
    
    # Run 'show ip interface brief' command
    output = connection.send_command("show ip interface brief")
    
    # Print the full output (optional for debugging)
    print("\nFull IP Interface Details:\n")
    print(output)
    
    # Process the output to filter down interfaces
    print("\nInterfaces that are DOWN:\n")
    lines = output.split("\n")  # Split output into lines
    
    for line in lines[1:]:  # Skip header row
        columns = line.split()  # Split each line into columns
        if len(columns) >= 6:  # Ensure line has enough columns
            interface, ip, ok, method, status, protocol = columns[:6]
            if status.lower() == "administratively" or protocol.lower() == "down":
                print(f"{interface} - Status: {status}, Protocol: {protocol}")

    # Close the SSH session
    connection.disconnect()

except Exception as e:
    print(f"Error: {e}")