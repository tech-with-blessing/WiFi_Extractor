"""
DISCLAIMER:
This script is for EDUCATIONAL PURPOSES ONLY.

✔ It only works on Wi-Fi networks that are already saved on YOUR OWN PC
✔ It does NOT hack, crack, or access other people's networks
✔ It simply asks Windows to reveal passwords you already have permission to see

❌ Do NOT use this on computers or networks you do not own
❌ Unauthorized access to networks is illegal and unethical

Author: Blessing Machekeche
"""

import subprocess

# -----------------------------
# STEP 1: Get all saved Wi-Fi profiles
# -----------------------------
# Windows uses a tool called "netsh" to manage Wi-Fi
# We ask it to show all saved Wi-Fi networks on this PC

command = ["netsh", "wlan", "show", "profiles"]

# Run the command and capture the output as text
output = subprocess.check_output(command, shell=True, text=True)

# -----------------------------
# STEP 2: Extract Wi-Fi names (SSIDs)
# -----------------------------
wifi_names = []

for line in output.splitlines():
    # Each saved Wi-Fi profile appears with "All User Profile"
    if "All User Profile" in line:
        # Split the line at ":" and take the Wi-Fi name
        name = line.split(":")[1].strip()
        wifi_names.append(name)

# -----------------------------
# STEP 3: For each Wi-Fi, get its password
# -----------------------------
print("\nSaved Wi-Fi Passwords (Owner Access Only):\n")

for wifi in wifi_names:
    try:
        # Command to show Wi-Fi details including password
        wifi_command = [
            "netsh",
            "wlan",
            "show",
            "profile",
            wifi,
            "key=clear"
        ]

        wifi_output = subprocess.check_output(
            wifi_command,
            shell=True,
            text=True
        )

        # Look for the password line
        password = "Not Found"
        for line in wifi_output.splitlines():
            if "Key Content" in line:
                password = line.split(":")[1].strip()

        print(f"Wi-Fi Name : {wifi}")
        print(f"Password  : {password}")
        print("-" * 30)

    except:
        # Some networks may not have passwords
        print(f"Wi-Fi Name : {wifi}")
        print("Password  : Unable to retrieve")
        print("-" * 30)