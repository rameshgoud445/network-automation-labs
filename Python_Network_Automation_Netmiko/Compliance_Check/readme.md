# Network Configuration Compliance Check Using Netmiko

## Overview

This project automates basic configuration compliance checks on multiple Cisco routers using Python, Netmiko, and YAML.

The script connects to each router, retrieves its running configuration, and checks whether specific security and management configuration patterns are present.

It helps network engineers identify missing configuration requirements and maintain consistent configurations across network devices.

## Project Structure

```text
Compliance_Check/
├── compliance_check.py
├── inventory.yml
└── README.md
```

## Features

- Connects to multiple Cisco routers using SSH.
- Loads device details from a YAML inventory file.
- Retrieves the running configuration.
- Checks for required AAA configuration.
- Checks for SSH access configuration.
- Checks for a Message of the Day (MOTD) banner.
- Checks for SNMP community configuration.
- Displays pass/fail results for each rule.
- Handles connection and execution errors.

## Technologies Used

- Python 3
- Netmiko
- PyYAML
- Cisco IOS
- GNS3

## Compliance Rules

The script checks for the following configuration patterns:

| Rule | Configuration pattern | Purpose |
|---|---|---|
| AAA | `aaa new-model` | Enables AAA functionality for authentication, authorization, and accounting. |
| SSH | `transport input ssh` | Allows SSH transport on applicable VTY lines. |
| Banner | `banner motd` | Checks for an MOTD banner configuration. |
| SNMP | `snmp-server community` | Checks for an SNMP community configuration. |

**Note:** These are basic text-presence checks, not complete security validations. For example, the script does not verify whether SNMP uses a secure configuration or whether AAA is configured correctly for the intended authentication policy.

## Prerequisites

- Python 3 installed.
- SSH connectivity to the target Cisco routers.
- Valid router credentials and enable access.
- Cisco IOS devices that support the commands being checked.

Install the required libraries:

```bash
pip install netmiko pyyaml
```

## Inventory Configuration

Create an `inventory.yml` file containing the device connection details.

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

Replace the sample IP addresses and credentials with your own lab details. Do not commit real passwords to GitHub.

## How to Run

Navigate to the project directory:

```bash
cd Compliance_Check
```

Run the script:

```bash
python3 compliance_check.py
```

## How It Works

1. Loads router details from `inventory.yml`.
2. Connects to each router using Netmiko.
3. Enters privileged EXEC mode.
4. Retrieves the running configuration using `show running-config`.
5. Searches the configuration for each required pattern.
6. Prints whether each rule is present or missing.
7. Continues to the next device if a connection or execution error occurs.

## Example Output

```text
Compliance Check: 192.168.12.130

aaa present
ssh present
banner present
snmp present

Compliance Check: 192.168.12.131

aaa missing
ssh present
banner present
snmp missing
```

*This is illustrative output. Actual results depend on the router configurations.*

## Troubleshooting

If a device fails the compliance check, verify the relevant configuration on the router:

```text
show running-config
show running-config | section aaa
show running-config | section line vty
show running-config | include banner
show running-config | include snmp-server
```

Command support and output formatting may vary by Cisco IOS version.

## Possible Improvements

- Use regular expressions or structured configuration parsing instead of simple substring checks.
- Validate the actual configuration values, not just the presence of a command.
- Add configurable compliance rules in YAML.
- Generate a compliance report in CSV or JSON.
- Add logging and timestamps.
- Calculate a compliance percentage for each device.
- Provide remediation suggestions for missing rules.
- Use secure SNMPv3 configuration checks instead of relying only on community strings.

## Security Note

Treat router configurations and inventory files as sensitive. Do not publish real credentials or sensitive configuration data in a public GitHub repository.

## Disclaimer

This project is intended for network automation learning, lab testing, and authorized network compliance checks.
