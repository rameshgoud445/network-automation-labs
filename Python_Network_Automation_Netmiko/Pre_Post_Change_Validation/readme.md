# Pre- and Post-Change Network Validation Using Netmiko

## Overview

This project automates network validation before and after a configuration change on Cisco routers using Python, Netmiko, and YAML.

The script connects to a router, executes predefined validation commands before making a change, configures a Loopback10 interface, and runs the same commands again to help identify changes in network behavior.

This approach helps network engineers assess the impact of configuration changes and verify basic network connectivity and routing status.

## Project Structure

```text id="v9d5s7"
Pre_Post_Change_Validation/
├── pre_post_checks.py
├── inventory.yml
└── README.md
```

## Features

- Connects to Cisco routers using Netmiko.
- Loads device details from a YAML inventory file.
- Runs pre-change validation checks.
- Executes a sample interface configuration change.
- Runs post-change validation checks.
- Checks IP connectivity using ping.
- Displays the routing table.
- Displays BGP neighbor information.
- Prints command output for comparison.

## Technologies Used

- Python 3
- Netmiko
- PyYAML
- Cisco IOS
- GNS3

## Prerequisites

- Python 3 installed.
- Netmiko and PyYAML installed.
- SSH access to the target router.
- Valid router credentials and enable access.
- A lab router that supports the configured commands.

Install the required packages:

```bash id="x8f9y2"
pip install netmiko pyyaml
```

## Inventory Configuration

Create an `inventory.yml` file containing the router connection details.

Example:

```yaml id="c8kd0g"
devices:
  - device_type: cisco_ios
    host: 192.168.12.130
    username: admin
    password: "YOUR_PASSWORD"
    secret: "YOUR_ENABLE_PASSWORD"
```

Replace the sample address and credentials with your lab details. Do not commit real passwords to GitHub.

## Validation Commands

The script runs these commands before and after the change:

| Command | Purpose |
|---|---|
| `ping 8.8.8.8` | Checks reachability to a public IP address from the router. |
| `show ip route` | Displays the router's routing table. |
| `show ip bgp summary` | Displays BGP neighbor and session information. |

**Note:** The ping test requires suitable routing and permitted outbound connectivity. Failure to reach `8.8.8.8` does not necessarily mean the router's local interfaces or routing protocol are broken.

## Sample Configuration Change

The script configures Loopback10 with the following commands:

```text id="k0xw2f"
interface loopback10
ip address 10.10.10.1 255.255.255.255
```

This is an example change. Adjust it to suit your lab and ensure the IP address does not conflict with existing configurations.

## How to Run

Navigate to the project directory:

```bash id="n4x0x4"
cd Pre_Post_Change_Validation
```

Run the script:

```bash id="h6o2up"
python3 pre_post_checks.py
```

## How It Works

1. Loads router details from `inventory.yml`.
2. Connects to the router using SSH.
3. Enters privileged EXEC mode.
4. Runs the pre-change validation commands.
5. Applies the sample Loopback10 configuration.
6. Runs the same validation commands after the change.
7. Displays the outputs for manual comparison.
8. Disconnects from the router.

## Example Output

```text id="8i4x9b"
--- Pre-Change Checks ---

$ ping 8.8.8.8
Ping output...

$ show ip route
Routing table output...

$ show ip bgp summary
BGP neighbor summary...

--- Post-Change Checks ---

$ ping 8.8.8.8
Ping output...

$ show ip route
Routing table output...

$ show ip bgp summary
BGP neighbor summary...
```

*The output above is illustrative. Actual output depends on router configuration and connectivity.*

## Troubleshooting

If a validation command produces unexpected results, check:

- Router reachability and SSH credentials.
- Interface status and IP addressing.
- Routing table entries and default routes.
- BGP neighbor state.
- Whether the validation target is reachable from the router.
- Whether the configuration change was accepted.

Useful commands include:

```text id="fd9b0v"
show ip interface brief
show ip route
show ip bgp summary
show running-config interface loopback10
```

## Current Limitations

- The script prints results but does not automatically compare pre-change and post-change outputs.
- It does not determine whether the configuration change succeeded beyond displaying command output.
- The example configuration is applied to every device in the inventory.
- There is no explicit exception handling or guaranteed connection cleanup.
- The script does not save the configuration with `write memory`.

## Possible Improvements

- Compare pre-change and post-change outputs automatically.
- Validate expected routes and BGP neighbor states.
- Add exception handling and guaranteed SSH cleanup.
- Record results in timestamped log files.
- Generate a pass/fail report.
- Make configuration changes configurable through YAML.
- Add optional configuration backup and rollback procedures.

## Security and Safety

Run this script in an authorized lab or maintenance window. Review the configuration commands before execution, especially when the inventory contains multiple routers. Protect credentials and avoid publishing sensitive configuration data.

## Disclaimer

This project is intended for network automation learning, lab testing, and authorized network change validation.
