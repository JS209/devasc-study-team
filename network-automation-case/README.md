# Network Automation Case

This project analyzes simulated network device data and generates an operational report.

## Features

- Analyzes 8 simulated network devices
- Tracks hostname, device type, management IP, location, status, CPU usage, memory usage, uptime, and backup status
- Calculates totals by device type
- Calculates totals by location
- Flags devices that require attention
- Uses Python lists, dictionaries, loops, conditionals, and functions

## Device Flagging Rules

A device is flagged when:

- CPU usage is greater than 85%
- Memory usage is greater than 80%
- Backup status is not successful
- Uptime is less than 7 days
- Device status is not operational

## Security

The local configuration file `local_config.py` contains fake sensitive information for classroom demonstration purposes.

This file is excluded from Git using `.gitignore` and must not be uploaded to GitHub.