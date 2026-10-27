# Cisco Loopback Interface Configuration Using Netmiko

## Overview

This project demonstrates how to automate loopback interface configuration on a Cisco router using Python and Netmiko.

The script connects to the router through SSH, configures Loopback 5 with an IP address and description, and verifies the interface configuration using the `show ip interface brief` command.

## Lab Setup

- **Device:** Cisco router
- **Automation language:** Python 3.x
- **Automation library:** Netmiko
- **Access method:** SSH
- **Configuration type:** Loopback interface

### Router Details

| Parameter | Value |
|---|---|
| Management IP | `192.168.12.130` |
| Interface | `Loopback5` |
| Interface IP | `5.5.5.5` |
| Subnet mask | `255.255.255.255` |
| Description | `Configured_by_netmiko` |

## Project Structure

```text
Interface_Configuration/
├── configure_loopback_interface.py
└── README.md
```

## Features

- Establishes an SSH connection to a Cisco router using Netmiko.
- Enters privileged EXEC mode.
- Creates Loopback 5.
- Assigns an IP address and subnet mask.
- Configures an interface description.
- Displays the interface status using `show ip interface brief`.
- Prints the configuration output for verification.

## Prerequisites

Install Python 3.x and Netmiko:

```bash
pip install netmiko
```

Ensure that SSH is enabled on the router and that the supplied credentials have the required privileges.

## Configuration Commands

The script sends the following commands to the router:

```text
interface loopback 5
ip address 5.5.5.5 255.255.255.255
description Configured_by_netmiko
```

## How to Run

Navigate to the project directory:

```bash
cd Interface_Configuration
```

Run the script:

```bash
python3 configure_loopback_interface.py
```

## Verification

The script executes:

```text
show ip interface brief
```

Check the output for Loopback5 and confirm that its IP address is `5.5.5.5`.

To verify the description, use:

```text
show running-config interface loopback 5
```

## Expected Outcome

Loopback 5 should be configured with the specified IP address and description. The script displays the interface summary and Netmiko configuration output.

## Future Improvements

- Move router credentials into environment variables or a secure inventory.
- Add exception handling and guaranteed connection cleanup.
- Verify the loopback IP address and description automatically.
- Support configuring multiple interfaces from a YAML inventory.
- Add logging for configuration results.

## Security Considerations

Do not commit real router passwords to a public GitHub repository. Use lab credentials or secure credential management.

## Disclaimer

This project is intended for educational purposes and network automation lab practice. Test configuration changes in a controlled environment before using them in production.
