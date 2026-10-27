# Network Device Health Check Using Python, Netmiko, and YAML

## Overview

This project automates health checks on multiple Cisco routers using Python, Netmiko, and YAML.

The script connects to each router using SSH, executes diagnostic commands, and displays CPU utilization, memory information, interface status, BGP neighbor information, and OSPF neighbor status.

It helps network engineers monitor device health and identify potential network issues from a single Python script.

## Project Structure

```text
Health_Check/
├── health_check.py
├── inventory.yml
└── README.md
```

## Features

- Connects to multiple Cisco routers using Netmiko.
- Loads router connection details from a YAML inventory file.
- Checks CPU utilization.
- Displays memory information.
- Checks interface status and IP addresses.
- Displays BGP neighbor information.
- Displays OSPF neighbor status.
- Handles connection and command execution errors.

## Technologies Used

- Python 3
- Netmiko
- PyYAML
- Cisco IOS
- GNS3

## Prerequisites

- Python 3 installed.
- SSH access to the routers.
- Valid router credentials.
- Cisco IOS devices that support the configured commands.

Install the required libraries:

```bash
pip install netmiko pyyaml
```

## Inventory Configuration

Create an `inventory.yml` file containing the router connection details.

Example:

```yaml
devices:
  - device_type: cisco_ios
    host: 192.168.12.130
    username: admin
    password: "YOUR_PASSWORD"
    secret: "YOUR_ENABLE_PASSWORD"

  - device_type: cisco_ios
    host: 192.168.12.131
    username: admin
    password: "YOUR_PASSWORD"
    secret: "YOUR_ENABLE_PASSWORD"
```

Replace the example IP addresses and credentials with your lab device details. Keep real passwords out of GitHub.

## Health Check Commands

The script executes the following Cisco IOS commands:

| Category | Command | Purpose |
|---|---|---|
| CPU | `show processes cpu sorted \| include one minute` | Displays CPU utilization information. |
| Memory | `show processes memory \| include Processor` | Displays matching processor memory information. |
| Interfaces | `show ip int brief \| exclude unassigned` | Displays interfaces with assigned IP addresses. |
| BGP | `show ip bgp summary` | Displays BGP neighbor and session information. |
| OSPF | `show ip ospf neighbor` | Displays OSPF neighbor states. |

*Note:* The exact output and available commands depend on the Cisco IOS version. The memory command filters output and may not display complete memory utilization statistics.

## How to Run

Navigate to the project directory:

```bash
cd Health_Check
```

Run the script:

```bash
python3 health_check.py
```

## Example Output

```text
Health Check for 192.168.12.130

--- CPU ---
CPU utilization information...

--- Memory ---
Processor memory information...

--- Interfaces ---
Interface IP-Address OK? Method Status Protocol
GigabitEthernet1/0 192.168.21.1 YES manual up up

--- BGP ---
BGP neighbor summary...

--- OSPF ---
OSPF neighbor information...
```

*The output above is illustrative. Actual results depend on the device configuration and operational status.*

## Troubleshooting

If a device fails to connect or a command does not return the expected output, check:

- Router IP address and SSH reachability.
- Username, password, and enable password.
- Python dependencies.
- Device support for the configured IOS commands.
- BGP and OSPF configuration, where applicable.
- Interface status and routing connectivity.

## Possible Improvements

- Add CPU and memory threshold alerts.
- Identify interfaces that are down.
- Validate expected BGP and OSPF neighbor states.
- Save health-check results to a log file or CSV report.
- Add timestamps to each check.
- Run checks concurrently to reduce execution time.
- Generate a final health summary for all routers.

## Security Note

Do not commit real router passwords or other sensitive credentials to GitHub. Use environment variables or a secure secrets-management method for production environments.

## Disclaimer

This project is intended for network automation learning, lab testing, and authorized network monitoring.
