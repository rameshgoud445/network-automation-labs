# Sequential Multi-Router Interface and BGP Configuration

## Overview

This project automates interface and BGP configuration across multiple Cisco routers using Python, Netmiko, and YAML.

Router connection details, interface IP addresses, BGP autonomous system numbers (ASNs), and neighbor information are stored in a YAML inventory file. The Python script reads this inventory and configures each router sequentially, one at a time, before displaying its BGP summary.

## Lab Setup

- **Devices:** 4 Cisco routers
- **Automation language:** Python 3.x
- **Automation library:** Netmiko
- **Inventory format:** YAML
- **Execution method:** Sequential execution
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
Sequential_Deployment/
├── yaml_driven_interface_bgp_configuration.py
├── bgp_multiple.yml
└── README.md
```

## Features

- Loads router details from a YAML inventory file.
- Establishes SSH connections using Netmiko.
- Configures interface IP addresses and enables interfaces using `no shutdown`.
- Configures BGP using each router's local ASN.
- Adds BGP neighbors using their IP addresses and remote ASNs.
- Processes routers sequentially using a regular Python `for` loop.
- Displays configuration output for each router.
- Runs `show ip bgp summary` to inspect BGP neighbor status.
- Handles and displays router-specific configuration errors.

## Prerequisites

Install Python 3.x and the required libraries:

```bash
pip install netmiko pyyaml
```

Ensure that:

- All routers are reachable from the automation server.
- SSH is enabled and the credentials are valid.
- The automation account has configuration privileges.
- Interface names and IP addresses match the lab topology.
- BGP ASNs and neighbor IP addresses are correct.

## YAML Inventory Configuration

The `bgp_multiple.yml` file stores router connection details, interface configurations, and BGP neighbor information.

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

Add the remaining routers using the same structure, with their correct management addresses, interface details, ASNs, and BGP neighbors.

**Note:** The example shows only R1. Your actual YAML inventory must contain every router you want to configure.

## How to Run

Navigate to the project directory:

```bash
cd Sequential_Deployment
```

Run the Python script:

```bash
python3 yaml_driven_interface_bgp_configuration.py
```

## Execution Workflow

1. Load router information from `bgp_multiple.yml`.
2. Iterate through the routers one at a time.
3. Establish an SSH connection to the current router.
4. Generate interface configuration commands from the YAML inventory.
5. Generate BGP configuration commands using the router's ASN and neighbor details.
6. Apply the interface and BGP configuration.
7. Execute `show ip bgp summary`.
8. Display the configuration output and BGP summary.
9. Disconnect from the router and proceed to the next router.

## Sequential Deployment vs. Parallel Deployment

| Feature | Sequential Deployment | Parallel Deployment |
|---|---|---|
| Execution | One router at a time | Multiple routers concurrently |
| Python approach | `for` loop | `ThreadPoolExecutor` |
| Complexity | Simpler to understand and troubleshoot | Requires handling concurrent tasks |
| Typical advantage | Predictable execution order | Can reduce total deployment time |
| Best suited for | Learning and controlled changes | Multi-device deployment tasks |

## Expected Outcome

The script attempts to configure the interfaces and BGP neighbors on each router in sequence. It displays the configuration output and BGP summary after configuring each router.

Review the output and confirm that the intended BGP neighbors reach the `Established` state.

## Future Improvements

- Add automated BGP neighbor-state validation.
- Take configuration backups before making changes.
- Save the configuration using `write memory` when appropriate.
- Add structured logging to a file.
- Ensure SSH connections are closed even if an error occurs.
- Generate a final report showing success or failure for each router.
- Add pre-change and post-change validation.
- Implement secure credential management.

## Security Considerations

- Never commit real router passwords to a public GitHub repository.
- Use placeholders in example inventory files.
- Consider excluding sensitive inventory files from Git using `.gitignore`.
- Test configuration changes in a controlled lab before using them in production.

## Disclaimer

This project is intended for educational purposes and network automation lab practice. Validate the configuration and BGP neighbor states before considering a deployment successful.
