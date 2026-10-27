# Routing Protocol Health Check Using Netmiko

## Overview

This project automates OSPF and BGP neighbor health checks on multiple Cisco routers using Python, Netmiko, and YAML.

The script connects to each router through SSH, executes routing protocol commands, checks whether OSPF and BGP appear operational, and records the results in a log file.

It helps network engineers identify potential routing protocol issues and simplifies routine network health monitoring.

## Project Structure

```text
Routing_Protocol_Health_Check/
├── routing_protocol_health_check.py
├── inventory.yml
├── README.md
└── health_check.log
```

The log file is generated when the script runs and does not need to be created manually.

## Features

- Connects to multiple Cisco routers using Netmiko.
- Loads device details from a YAML inventory.
- Checks OSPF neighbor status.
- Checks BGP neighbor status.
- Displays results in the terminal.
- Logs successful checks, warnings, and errors.
- Handles connection timeouts.
- Handles authentication failures.
- Reports unexpected errors.

## Technologies Used

- Python 3
- Netmiko
- PyYAML
- Python logging
- Cisco IOS
- GNS3

## Prerequisites

- Python 3 installed.
- SSH access to the target routers.
- Valid router credentials and enable access.
- OSPF and/or BGP configured on the devices being checked.

Install the required packages:

```bash
pip install netmiko pyyaml
```

## Inventory Configuration

Create an `inventory.yml` file with the router connection details.

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

Replace the sample addresses and credentials with your lab details. Do not commit real passwords to GitHub.

## Routing Protocol Commands

| Protocol | Command | Purpose |
|---|---|---|
| OSPF | `show ip ospf neighbor` | Displays OSPF neighbor states. |
| BGP | `show ip bgp summary` | Displays BGP neighbor and session information. |

## How to Run

Navigate to the project directory:

```bash
cd Routing_Protocol_Health_Check
```

Run the script:

```bash
python3 routing_protocol_health_check.py
```

## How It Works

1. Loads the router inventory from `inventory.yml`.
2. Connects to each router through SSH.
3. Enters privileged EXEC mode.
4. Executes `show ip ospf neighbor`.
5. Checks the output for the `FULL` state.
6. Executes `show ip bgp summary`.
7. Checks the output for the text `Establ`.
8. Displays the results and records them in `health_check.log`.
9. Handles timeouts, authentication failures, and unexpected errors.

## Example Output

```text
Connecting to 192.168.12.130

OSPF neighbor output...
OSPF OK

BGP neighbor output...
BGP OK

Health check completed
```

*The output is illustrative. Actual results depend on device configuration and neighbor states.*

## Log File

The script creates `health_check.log` and records events with timestamps and log levels.

Example:

```text
2026-10-27 14:00:00,000 - INFO - 192.168.12.130 - OSPF OK
2026-10-27 14:00:01,000 - INFO - 192.168.12.130 - BGP OK
2026-10-27 14:00:05,000 - WARNING - 192.168.12.131 - OSPF ISSUE
```

The exact timestamps and messages will vary.

## Troubleshooting

If a router fails a check, verify its status using:

```text
show ip ospf neighbor
show ip bgp summary
show ip interface brief
show ip route
```

Also check SSH reachability, credentials, interface status, routing configuration, and the log file.

## Current Limitations

- The script checks whether `FULL` or `Establ` appears anywhere in the command output. It does not validate every expected neighbor individually.
- If a device has no OSPF or BGP configured, the script reports an issue even if that protocol is not required on the device.
- The connection is explicitly disconnected after successful checks, but not in every exception path.
- The script checks status but does not automatically repair routing problems.

## Possible Improvements

- Validate each expected OSPF and BGP neighbor individually.
- Define which protocols are required for each router in YAML.
- Add a final summary of healthy and unhealthy devices.
- Ensure connections are closed in a `finally` block.
- Export results to CSV or JSON.
- Add configurable alert thresholds and automated notifications.

## Security Note

Protect router credentials and log files. Do not publish passwords or sensitive device information in a public repository.

## Disclaimer

This project is intended for network automation learning, lab testing, and authorized network monitoring.
