# Multi-Device BGP Deployment Using Netmiko

## Overview

This project automates BGP configuration across multiple Cisco routers using Python, Netmiko, YAML, and multithreading.

The script dynamically generates BGP neighbor configurations, takes configuration backups before making changes, saves configurations, and verifies BGP status.

## Lab Setup

- **Devices:** 4 Cisco routers
- **Automation:** Python 3.x
- **Libraries:** Netmiko, PyYAML
- **Protocol:** SSH
- **Configuration source:** YAML inventory

### Router Management IPs

| Router | Management IP  |
|--------|----------------|
| R1     | 192.168.12.130 |
| R2     | 192.168.12.131 |
| R3     | 192.168.12.132 |
| R4     | 192.168.12.133 |

## Project Structure

```text
BGP_Multi_Device_Deployment/
├── multi_device_bgp_deployment_with_backup.py
├── inventory.yml
├── README.md
```

## Features

- Loads router details and BGP AS numbers from a YAML inventory.
- Establishes SSH connections using Netmiko.
- Takes a backup of each router's running configuration before changes.
- Generates BGP neighbor configuration dynamically.
- Configures multiple routers concurrently using `ThreadPoolExecutor`.
- Saves configurations using `write memory`.
- Verifies BGP status using `show ip bgp summary`.
- Records backup completion and errors in a log file.

## Prerequisites

Install Python 3.x and the required libraries:

```bash
pip install netmiko pyyaml
```

Ensure that SSH access is available to all routers and that the routers support the required Cisco IOS commands.

## Configuration

Update `inventory.yml` with the router management IPs, SSH credentials, and BGP AS numbers.

Do not commit real passwords or other secrets to a public GitHub repository.

## Execution

Navigate to the project directory:

```bash
cd BGP_Multi_Device_Deployment
```

Run the automation script:

```bash
python3 multi_device_bgp_deployment_with_backup.py
```

## Execution Workflow

1. Load router inventory from YAML.
2. Connect to routers using SSH.
3. Back up each router's running configuration.
4. Generate and push BGP configuration.
5. Save the configuration.
6. Display the BGP summary for verification.
7. Record errors in the log file.

## Expected Outcome

The script attempts to configure BGP on all routers concurrently, saves pre-change configuration backups, and displays each router's BGP summary.

Verify that the intended BGP neighbors reach the `Established` state before treating deployment as successful.

## Future Improvements

- Add explicit BGP neighbor-state validation.
- Add pre-change and post-change reachability checks.
- Improve exception handling and connection cleanup.
- Add configuration rollback support.
- Add secure credential management.
- Generate a deployment summary showing success or failure per router.

## Disclaimer

This project is intended for learning and lab testing. Test configurations in a controlled environment before using them on production devices.
