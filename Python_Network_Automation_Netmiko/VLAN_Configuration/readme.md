# VLAN Configuration using Python and Netmiko

## Overview
This project automates VLAN creation on Cisco network devices using Python and Netmiko. It includes two approaches: configuring VLANs using device IP addresses directly in Python and deploying VLANs using a YAML inventory file.

## Folder Structure

```text
VLAN_Configuration/
│
├── README.md
├── configure_vlan.py
├── vlan_deploy.py
└── inventory.yml
```

## Programs

### 1. `configure_vlan.py`
- Connects to multiple Cisco switches using Netmiko.
- Creates VLAN 20 with the name `TECH-Team`.
- Saves the configuration.
- Displays VLAN information for verification.

**VLAN details:**
- VLAN ID: `20`
- VLAN Name: `TECH-Team`

**Note:** Device IP addresses are configured directly in the Python script.

### 2. `vlan_deploy.py`
- Reads device connection details from `inventory.yml`.
- Connects to multiple Cisco devices using Netmiko.
- Creates VLAN 100 with the name `Automation_VLAN`.

**VLAN details:**
- VLAN ID: `100`
- VLAN Name: `Automation_VLAN`

This approach separates device information from the Python code, making it easier to manage multiple devices.

### 3. `inventory.yml`
Stores device connection details used by `vlan_deploy.py`, including:
- Device type
- Management IP address
- Username
- Password
- Enable password

Example:

```yaml
devices:
  - device_type: cisco_ios
    host: 192.168.12.140
    username: admin
    password: YOUR_PASSWORD
    secret: YOUR_ENABLE_PASSWORD

  - device_type: cisco_ios
    host: 192.168.12.141
    username: admin
    password: YOUR_PASSWORD
    secret: YOUR_ENABLE_PASSWORD

  - device_type: cisco_ios
    host: 192.168.12.142
    username: admin
    password: YOUR_PASSWORD
    secret: YOUR_ENABLE_PASSWORD
```

Replace the example credentials with your lab credentials locally. Do not commit real passwords to GitHub.

## Requirements

Install the required Python packages:

```bash
pip install netmiko pyyaml
```

## How to Run

Navigate to the VLAN configuration directory:

```bash
cd VLAN_Configuration
```

Run the first program:

```bash
python configure_vlan.py
```

Run the YAML-driven program:

```bash
python vlan_deploy.py
```

If your environment uses Python 3 explicitly, use `python3` instead of `python`.

## Verification

On the Cisco switch, run:

```text
show vlan brief
```

Verify that the expected VLAN ID and VLAN name appear in the output.

## Important Notes
- Ensure SSH connectivity and valid credentials for all devices.
- Confirm the target devices support the Cisco IOS commands used by the scripts.
- Test changes in a lab environment before using them in production.
- The first program saves its configuration; check `vlan_deploy.py` before relying on its changes being saved permanently.
- Never commit passwords or other sensitive device information to GitHub.

## Technologies Used
- Python
- Netmiko
- PyYAML
- Cisco IOS

## Learning Objective
This project demonstrates how to automate VLAN creation on multiple network devices using Python, Netmiko, and YAML-based device inventory management.