import os
import subprocess

# Step 1: Run the playbook
print("📡 Running Ansible playbook to fetch BGP summary...")
subprocess.run(["ansible-playbook", "-i", "hosts.ini", "bgp_summary.yml"], check=True)

# Step 2: Read the output
output_file = "/tmp/bgp_summary_output.txt"

down_states = ["Idle", "Active", "Connect"]

print("\n🔍 Checking BGP neighbors that are down:\n")

try:
    with open(output_file, "r") as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
        if line.strip().startswith("Neighbor"):
            data_lines = lines[index + 1:]
            break
    else:
        print("No BGP data found.")
        data_lines = []

    for line in data_lines:
        if not line.strip():
            continue

        fields = line.split()
        if len(fields) < 9:
            continue

        neighbor_ip = fields[0]
        last_field = fields[-1]
        second_last = fields[-2]

        if last_field in down_states:
            print(f"Neighbor {neighbor_ip} is in state: {last_field}")
        elif not last_field.isdigit() and second_last in down_states:
            print(f"Neighbor {neighbor_ip} is in state: {second_last}")

except FileNotFoundError:
    print("❌ BGP summary file not found.")
