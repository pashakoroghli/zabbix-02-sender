#!/usr/bin/env python3
"""
zabbix_mock_data_sender.py

A simple utility script for sending mock (hardcoded) metrics to a Zabbix server
using `zabbix_sender`. This script is useful for testing Zabbix trapper items,
debugging, and verifying metric ingestion from local systems.

Author: PASHA
License: MIT (or any license you prefer)
"""

import subprocess
import datetime


# ==========================
# Configuration Parameters
# ==========================

# Path to the `zabbix_sender` executable.
zabbix_sender_path = "/usr/bin/zabbix_sender"

# Zabbix server address (IP or hostname).
zabbix_server_ip = "x.x.x.x"

# The host *as defined in Zabbix* to which metrics will be sent.
zabbix_hostname = "HOSTNAME"

# Zabbix trapper keys.
key_status = "sms.job.status"
key_time_str = "sms.job.time_str"
key_individual = "sms.job.individual_value"


def send_to_zabbix(key: str, value):
    """
    Sends a single metric to Zabbix using the `zabbix_sender` CLI.

    Parameters:
        key (str): Zabbix trapper key.
        value: Value to send (int, float, str).

    Prints:
        - The executed command
        - Zabbix sender output (stdout / stderr)
        - Exit code
    """

    cmd = [
        zabbix_sender_path,
        "-z", zabbix_server_ip,
        "-s", zabbix_hostname,
        "-k", key,
        "-o", str(value),
    ]

    print("\nRunning command:", " ".join(cmd))

    result = subprocess.run(cmd, capture_output=True, text=True)

    print(f"[{key}] => {value}")
    print("Exit code:", result.returncode)

    if result.stdout:
        print("STDOUT:\n", result.stdout.strip())

    if result.stderr:
        print("STDERR:\n", result.stderr.strip())


if __name__ == "__main__":
    # ==========================
    # Mock / Hardcoded Values
    # ==========================

    # Example numeric values
    status_value = 1
    individual_value = 13

    # Current timestamp formatted as: YYYY-MM-DD HH:MM:SS
    time_value = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ==========================
    # Send Metrics to Zabbix
    # ==========================

    send_to_zabbix(key_status, status_value)
    send_to_zabbix(key_time_str, time_value)
    send_to_zabbix(key_individual, individual_value)
