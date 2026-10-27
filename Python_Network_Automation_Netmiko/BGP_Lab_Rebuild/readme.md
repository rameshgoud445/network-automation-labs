# Automated Router Rebuild and BGP Validation

## Overview

This project automates the process of rebuilding Cisco routers and validating BGP connectivity using Python and Netmiko.

The script is designed for a **GNS3 lab environment** with multiple Cisco routers. It resets the router configurations, reloads the devices, applies interface and BGP configurations, saves the configuration, and checks BGP neighbor status.

## Project Structure

```text
BGP_Lab_Rebuild/
├── automated_router_rebuild_and_bgp_validation.py
└── README.md
```

## Features

- Connects to multiple Cisco routers using Netmiko.
- Erases existing router configurations.
- Reloads routers and waits for them to become available.
- Configures router interfaces and BGP.
- Saves the configuration using `write memory`.
- Executes `show ip bgp summary` to check BGP status.
- Identifies routers that may have BGP connectivity issues.

## Technologies Used

- Python 3
- Netmiko
- Cisco IOS
- GNS3

## Prerequisites

Before running the script, ensure that:

- Python 3 is installed.
- Netmiko is installed.
- Cisco routers are configured and reachable in the GNS3 lab.
- SSH access and credentials are available.
- The router IP addresses and configuration commands match your lab topology.

Install Netmiko:

```bash
pip install netmiko
```

## How It Works

1. **Router connection:** Connects to each router using SSH.
2. **Configuration reset:** Erases the existing startup configuration.
3. **Router reload:** Reloads the device and waits for it to become available.
4. **Configuration deployment:** Applies the required interface and BGP configurations.
5. **Configuration save:** Saves the new configuration.
6. **BGP validation:** Runs `show ip bgp summary` and checks the BGP status.
7. **Issue identification:** Reports routers that may require further troubleshooting.

## How to Run

Navigate to the project directory:

```bash
cd BGP_Lab_Rebuild
```

Run the script:

```bash
python3 automated_router_rebuild_and_bgp_validation.py
```

## Verification

On each router, verify the interface status:

```text
show ip interface brief
```

Verify BGP neighbor status:

```text
show ip bgp summary
```

A BGP neighbor in the `Established` state indicates that the BGP session is up. For eBGP, confirm the expected neighbor relationships and routes as well.

## Important Safety Warning

**This script performs destructive operations.**

The commands `write erase` and `reload` remove existing router configuration and restart the devices.

- Run this script only in an isolated GNS3 lab or on devices explicitly approved for rebuilding.
- Do not run it on production routers.
- Back up configurations before starting.
- Confirm that the router IP addresses, credentials, interfaces, AS numbers, and BGP neighbor addresses are correct.
- Ensure that the script can reconnect after each reload.

## Possible Improvements

- Add automatic retry logic for SSH reconnections.
- Validate every expected BGP neighbor individually.
- Verify interface status and advertised routes.
- Add detailed logging and a final deployment report.
- Add exception handling and guaranteed SSH session cleanup.
- Load router details and configuration from a YAML inventory file.

## Disclaimer

This project is intended for network automation practice and lab testing. Use it only in an environment where you have authorization to erase and rebuild router configurations.
