# BGP Neighbor State Monitoring Using Netmiko

## Overview

This project uses Python and Netmiko to monitor BGP neighbor states on a Cisco router. The script connects to the router through SSH, executes the `show ip bgp summary` command, and identifies BGP neighbors that are in the `Idle`, `Active`, or `Connect` state.

It helps network engineers identify potential BGP connectivity issues and troubleshoot routing problems.

## Project Structure

```text
BGP_Neighbor_Monitoring/
├── bgp_neighbor_state_monitor.py
└── README.md
```

## Features

- Connects to a Cisco router using SSH.
- Executes the `show ip bgp summary` command.
- Checks for BGP neighbor states such as `Idle`, `Active`, and `Connect`.
- Displays BGP summary output.
- Identifies potential BGP neighbor issues.

## Technologies Used

- Python 3
- Netmiko
- Cisco IOS
- GNS3

## Prerequisites

- Python 3 installed.
- Netmiko installed.
- SSH connectivity to the target router.
- Valid router credentials and IP address.

Install Netmiko:

```bash
pip install netmiko
```

## How to Run

Navigate to the project directory:

```bash
cd BGP_Neighbor_Monitoring
```

Run the script:

```bash
python3 bgp_neighbor_state_monitor.py
```

## Commands Used

The script executes the following Cisco IOS command:

```text
show ip bgp summary
```

This command displays BGP neighbor information, including the remote AS, message counters, and session state or prefix count.

## Example Output

```text
Connecting to router...
BGP Summary:
Neighbor        AS       State
192.168.21.1    500      Established
192.168.23.3    500      Active

BGP neighbor issues detected.
```

*Note: This is an illustrative example. Actual output depends on your router configuration and BGP sessions.*

## BGP Neighbor States

| State | Meaning |
|---|---|
| Established | BGP session is up and exchanging routing information. |
| Idle | BGP is not currently establishing a session. |
| Connect | BGP is attempting to establish a TCP connection. |
| Active | BGP is attempting to establish a connection, often after a connection attempt fails. |

## Troubleshooting

If a neighbor remains in `Idle`, `Active`, or `Connect`, check:

- Neighbor IP address and remote AS number.
- IP reachability between BGP peers.
- TCP port 179 connectivity.
- Interface status and routing to the neighbor.
- BGP authentication or other session parameters, if configured.

Useful Cisco IOS commands:

```text
show ip bgp summary
show ip bgp neighbors
show ip route
ping <neighbor-ip>
```

## Possible Improvements

- Monitor multiple routers using a YAML inventory.
- Check each neighbor's state individually.
- Add logging and timestamps.
- Generate alerts when a BGP session is down.
- Schedule periodic monitoring.
- Export results to CSV or a monitoring dashboard.

## Disclaimer

This project is intended for network automation learning and lab testing. Ensure you have authorization before connecting to network devices.
