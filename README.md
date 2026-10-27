# Python Network Automation with Netmiko

A hands-on learning repository for students, networking freshers, and network engineers who want to learn Python-based network automation through practical lab projects.

This repository contains automation examples using **Python, Netmiko, and YAML** to help you practice network configuration, device monitoring, validation, and multi-device operations in a controlled lab environment.

The goal is to help you move beyond manual CLI configuration and develop practical network automation skills.

## What You Will Learn

- Connect to network devices using Python and Netmiko
- Automate repetitive network administration tasks
- Deploy BGP configurations across multiple routers
- Configure VLANs and loopback interfaces
- Monitor BGP neighbor states and routing protocol health
- Perform network device health checks
- Back up device configurations
- Validate configurations before and after network changes
- Perform compliance checks against expected configurations
- Automate tasks across multiple network devices
- Use YAML files to maintain device inventories and configuration parameters

## Project Structure

The projects are organized by networking task so you can learn and practice one concept at a time.

| Project | What you can practice |
|---|---|
| `BGP_Configuration/` | Sequential and parallel BGP configuration deployment |
| `BGP_Lab_Rebuild/` | Automated router rebuild and BGP validation |
| `BGP_Neighbor_Monitoring/` | Monitoring BGP neighbor states |
| `Compliance_Check/` | Checking configurations against expected standards |
| `Config_Backup/` | Automating network device configuration backups |
| `Health_Check/` | Performing device health checks |
| `Interface_Configuration/` | Automating loopback interface configuration |
| `Multi_Device_Deployment/` | Deploying configurations across multiple devices |
| `Pre_Post_Change_Validation/` | Validating device state before and after changes |
| `Routing_Protocols_Health_Check/` | Detecting and checking OSPF and BGP status |
| `VLAN_Configuration/` | Automating VLAN configuration and deployment |

Refer to the README inside each project folder for project-specific details and instructions.

## Technologies Used

- **Python** — automation logic and scripting
- **Netmiko** — SSH-based network device interaction
- **PyYAML** — reading YAML inventory and configuration files
- **SSH** — remote access to supported network devices
- **YAML** — maintaining device inventories and configuration parameters

Individual scripts may require additional Python packages or device-specific configuration.

## Prerequisites

Before running the projects, you should have:

- Basic knowledge of networking concepts such as IP addressing, VLANs, routing, BGP, and OSPF
- Basic Python knowledge
- Python 3 installed
- Access to supported network devices or a virtual networking lab
- SSH connectivity and authorized credentials for your lab devices

You can practice with compatible Cisco IOS devices or other platforms supported by your specific Netmiko connection driver.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rameshgoud445/network-automation-labs.git
```

### 2. Navigate to the project directory

```bash
cd network-automation-labs/Python_Network_Automation_Netmiko
```

### 3. Create a Python virtual environment

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 4. Install the common dependencies

```bash
python -m pip install --upgrade pip
python -m pip install netmiko pyyaml
```

Some projects may need additional dependencies. Review the individual scripts and project README files before running them.

### 5. Configure your device inventory

Many projects use an `inventory.yml` or another YAML file to define device connection parameters.

Before running a script:

1. Read the corresponding project README.
2. Review the YAML structure expected by the script.
3. Replace example addresses and parameters with your own lab device details.
4. Supply credentials securely.
5. Verify SSH reachability and permissions.

Do not publish real passwords, API tokens, private keys, or production device information in public inventory files.

### 6. Run a project

Navigate into the relevant project folder and follow its README instructions.

For example:

```bash
cd Health_Check
python health_check.py
```

The command above is an example of how to run the health-check script; the required inventory values and connection parameters must be configured first.

**Important:** Some scripts perform configuration changes on network devices. Review the source code before execution and use a test lab.

## Recommended Learning Path

1. Start with interface configuration and VLAN automation.
2. Practice device health checks and BGP neighbor monitoring.
3. Learn configuration backup and compliance checking.
4. Explore multi-device deployment.
5. Practice sequential and parallel BGP configuration.
6. Finish with pre-change and post-change validation and automated lab rebuilds.

## Lab Safety and Responsible Use

This repository is intended for educational use and authorized network administration.

- Use a lab environment whenever possible.
- Run scripts only on devices you own or are authorized to administer.
- Review every script before execution.
- Validate device addresses, configuration values, and credentials.
- Back up configurations before making changes.
- Use least-privilege accounts where supported.
- Keep secrets out of source code and public repositories.
- Test configuration changes before using them in production.

The scripts are learning examples. Review and adapt them for your device models, software versions, network topology, and operational requirements.

## Contributing

Students and network engineers are welcome to improve the learning experience by contributing:

- Bug fixes and tested improvements
- Additional network automation examples
- Better documentation and troubleshooting notes
- Lab topologies and sample configurations with sensitive information removed
- Support for additional network platforms

Before submitting changes, test your code in a suitable lab and remove credentials or sensitive data.

## Disclaimer

This repository is provided for educational and lab practice purposes. The examples are supplied without guarantees of suitability for a particular production environment. You are responsible for reviewing, testing, and validating code before using it on any network device.

## Author and Learning Resources

Maintained by **Ramesh Goud and the Tungabadra Networks learning community**.

Explore the projects, practice the scripts in your lab, and build your network automation skills step by step.

GitHub Repository: https://github.com/rameshgoud445/network-automation-labs

Website: https://tungabadranetworks.in/
