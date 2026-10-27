# Automated Network Configuration Backup Using Netmiko

## Overview

This project automates configuration backups for multiple Cisco routers using Python, Netmiko, and YAML.

The script connects to each router through SSH, retrieves its running configuration using `show running-config`, and saves the output to a file with the device IP address and timestamp in the filename.

This helps network engineers maintain configuration backups for troubleshooting, auditing, and recovery purposes.

## Project Structure

```text
Config_Backup/
├── backup_configs.py
├── inventory.yml
├── backups/
└── README.md
```

## Features

- Connects to multiple Cisco routers using Netmiko.
- Loads device connection details from a YAML inventory file.
- Retrieves running configurations.
- Saves each backup as a `.cfg` file.
- Adds the device IP address and timestamp to each filename.
- Handles connection and backup errors.

## Technologies Used

- Python 3
- Netmiko
- PyYAML
- Cisco IOS
- GNS3

## Prerequisites

- Python 3 installed.
- SSH access to the target routers.
- Valid router credentials and enable access.
- A `backups` directory to store the configuration files.

Install the required libraries:

```bash
pip install netmiko pyyaml
```

## Inventory Configuration

Create an `inventory.yml` file with the router details.

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

Replace the example IP addresses and credentials with your own lab details. Do not commit real passwords to GitHub.

## How It Works

1. Loads router details from `inventory.yml`.
2. Connects to each router using SSH.
3. Enters privileged EXEC mode using `enable()`.
4. Executes `show running-config`.
5. Creates a backup filename containing the router IP and current timestamp.
6. Saves the running configuration in the `backups` directory.
7. Displays a success or failure message for each device.

## How to Run

Navigate to the project directory:

```bash
cd Config_Backup
```

Create the backup directory if it does not exist:

```bash
mkdir -p backups
```

Run the script:

```bash
python3 backup_configs.py
```

## Example Output

```text
Backup saved for 192.168.12.130 at backups/192.168.12.130_20261027_140000.cfg
Backup saved for 192.168.12.131 at backups/192.168.12.131_20261027_140005.cfg
```

*The timestamps above are examples. Actual filenames depend on when the script runs.*

## Backup File Naming Convention

The script uses the following format:

```text
<device_ip>_<YYYYMMDD_HHMMSS>.cfg
```

For example:

```text
192.168.12.130_20261027_140000.cfg
```

This makes it easier to identify the device and backup time. Running the script again creates a new timestamped file rather than overwriting the previous backup.

## Troubleshooting

If a backup fails, check:

- Router IP address and SSH connectivity.
- Username, password, and enable password.
- Netmiko and PyYAML installation.
- Whether the `backups` directory exists.
- Whether the user running the script has permission to write files.

## Possible Improvements

- Automatically create the `backups` directory in Python.
- Add logging with timestamps.
- Use exception-safe connection cleanup.
- Back up startup configuration as well as running configuration.
- Compare current and previous backups to identify configuration changes.
- Add backup retention policies.
- Schedule backups to run automatically.

## Security Note

Router configuration files may contain sensitive information. Store backups securely, exclude the `backups/` directory and real credential files from GitHub, and use secure credential handling.

## Disclaimer

This project is intended for network automation learning and authorized network administration. Verify backup files and permissions before using this workflow in production.
