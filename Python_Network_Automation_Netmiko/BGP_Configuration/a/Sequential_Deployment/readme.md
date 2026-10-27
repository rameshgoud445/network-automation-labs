# Parallel Multi-Router Interface and BGP Automation

## Overview

This project automates interface and BGP configuration across multiple Cisco routers using Python, Netmiko, YAML, and multithreading.

Router details, interface IP addresses, BGP autonomous system numbers (ASNs), and neighbor information are stored in a YAML inventory file. The script connects to multiple routers concurrently, applies the configurations, and displays the BGP summary for verification.

## Lab Setup

- **Devices:** 4 Cisco routers
- **Automation language:** Python 3.x
- **Automation library:** Netmiko
- **Inventory format:** YAML
- **Execution method:** Multithreading using `ThreadPoolExecutor`
- **Access method:** SSH

### Router Management IPs

| Router | Management IP |
|---|---|
| R1 | `192.168.12.130` |
| R2 | `192.168.12.131` |
| R3 | `192.168.12.132` |
| R4 | `192.168.12.133` |

## Project Structure

```text
Parallel_Deployment/
├── parallel_multi_router_interface_bgp_automation.py
├── bgp_multiple.yml
└── README.md
```

## Features

- Loads router details from a YAML inventory file.
- Establishes SSH connections using Netmiko.
- Configures interface IP addresses and enables interfaces using `no shutdown`.
- Configures BGP using each router's local ASN.
- Adds BGP neighbors using their IP addresses and remote ASNs.
- Configures multiple routers concurrently.
- Uses `ThreadPoolExecutor` with a maximum of four worker threads.
- Displays configuration output for each router.
- Runs `show ip bgp summary` to inspect BGP neighbor status.
- Handles and displays router-specific configuration errors.

## Prerequisites

Install Python 3.x and the required libraries.

```bash
pip install netmiko pyyaml
```

Ensure that:

- All routers are reachable from the automation server.
- SSH is enabled and credentials are valid.
- The automation account has the required configuration privileges.
- The router interfaces and IP addressing match the lab topology.
- BGP ASNs and neighbor IP addresses are correct.

## YAML Inventory Configuration

The `bgp_multiple.yml` file contains router connection details, interface configurations, and BGP neighbor information.

Example:

```yaml
routers:
  R1:
    device_type: cisco_ios
    host: 192.168.12.130
    username: admin
    password: YOUR_LAB_PASSWORD
    asn: 100
    interfaces:
      - name: Loopback0
        ip: 1.1.1.1
        mask: 255.255.255.255
      - name: GigabitEthernet1/0
        ip: 192.168.21.1
        mask: 255.255.255.0
    neighbors:
      - ip: 192.168.21.2
        remote_as: 200
```

Add the remaining routers using the same structure, with their actual interface details, ASNs, and BGP neighbors.

**Note:** The interface names and addresses in the YAML must match your GNS3 router configuration. The example shows only R1; use the complete inventory for your lab.

## How to Run

Navigate to the project directory:

```bash
cd Parallel_Deployment
```

Run the automation script:

```bash
python3 parallel_multi_router_interface_bgp_automation.py
```

## Execution Workflow

1. Load router information from `bgp_multiple.yml`.
2. Create a separate configuration task for each router.
3. Establish SSH connections to routers using Netmiko.
4. Generate interface configuration commands from the YAML inventory.
5. Generate BGP configuration commands from the local ASN and neighbor details.
6. Apply the configuration to each router.
7. Execute `show ip bgp summary`.
8. Display the configuration output and BGP summary for each router.

## Expected Outcome

The script attempts to configure all listed routers concurrently, subject to the configured maximum of four worker threads.

Each router's configuration output and BGP summary are displayed in the terminal. Review the summary and confirm that the expected neighbors reach the `Established` state.

## Sequential vs. Parallel Deployment

| Feature | Sequential Deployment | Parallel Deployment |
|---|---|---|
| Execution | One router at a time | Multiple routers concurrently |
| Python approach | `for` loop | `ThreadPoolExecutor` |
| Completion | Waits for each router task | Collects completed tasks using `as_completed()` |
| Typical advantage | Easier troubleshooting | Can reduce total deployment time |
| Best suited for | Small changes and debugging | Multi-device configuration tasks |

## Future Improvements

- Add explicit BGP neighbor-state validation.
- Save running configurations before making changes.
- Save configurations using `write memory` when appropriate.
- Add structured logging to a file.
- Ensure SSH connections are closed even when errors occur.
- Produce a final report showing success or failure for every router.
- Add configuration rollback and pre/post-change validation.
- Use environment variables or a secrets manager for credentials.

## Security Considerations

- Never commit real router passwords to a public repository.
- Use lab credentials or placeholders in example inventory files.
- Consider excluding sensitive inventory files from Git using `.gitignore`.
- Test configuration changes in a controlled lab before using them in production.

## Disclaimer

This project is intended for educational purposes and network automation lab practice. Validate all configuration commands and BGP neighbor states before considering a deployment successful.
