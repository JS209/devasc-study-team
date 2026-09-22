# Network Automation Operational Report

devices = [
    {
        "hostname": "CORE-RTR-01",
        "device_type": "Router",
        "management_ip": "10.10.1.1",
        "location": "Los Angeles",
        "status": "Operational",
        "cpu_usage": 42,
        "memory_usage": 61,
        "uptime_days": 120,
        "backup_status": "Successful"
    },
    {
        "hostname": "CORE-RTR-02",
        "device_type": "Router",
        "management_ip": "10.10.1.2",
        "location": "Los Angeles",
        "status": "Operational",
        "cpu_usage": 91,
        "memory_usage": 72,
        "uptime_days": 87,
        "backup_status": "Successful"
    },
    {
        "hostname": "SW-LA-01",
        "device_type": "Switch",
        "management_ip": "10.10.2.1",
        "location": "Los Angeles",
        "status": "Operational",
        "cpu_usage": 35,
        "memory_usage": 48,
        "uptime_days": 200,
        "backup_status": "Successful"
    },
    {
        "hostname": "SW-LA-02",
        "device_type": "Switch",
        "management_ip": "10.10.2.2",
        "location": "Los Angeles",
        "status": "Degraded",
        "cpu_usage": 65,
        "memory_usage": 88,
        "uptime_days": 45,
        "backup_status": "Failed"
    },
    {
        "hostname": "FW-SD-01",
        "device_type": "Firewall",
        "management_ip": "10.20.1.1",
        "location": "San Diego",
        "status": "Operational",
        "cpu_usage": 52,
        "memory_usage": 63,
        "uptime_days": 150,
        "backup_status": "Successful"
    },
    {
        "hostname": "FW-SD-02",
        "device_type": "Firewall",
        "management_ip": "10.20.1.2",
        "location": "San Diego",
        "status": "Down",
        "cpu_usage": 0,
        "memory_usage": 0,
        "uptime_days": 0,
        "backup_status": "Failed"
    },
    {
        "hostname": "SW-SD-01",
        "device_type": "Switch",
        "management_ip": "10.20.2.1",
        "location": "San Diego",
        "status": "Operational",
        "cpu_usage": 44,
        "memory_usage": 81,
        "uptime_days": 92,
        "backup_status": "Successful"
    },
    {
        "hostname": "RTR-SF-01",
        "device_type": "Router",
        "management_ip": "10.30.1.1",
        "location": "San Francisco",
        "status": "Operational",
        "cpu_usage": 58,
        "memory_usage": 55,
        "uptime_days": 4,
        "backup_status": "Successful"
    }
]


def check_device(device):
    reasons = []

    if device["cpu_usage"] > 85:
        reasons.append("High CPU usage")

    if device["memory_usage"] > 80:
        reasons.append("High memory usage")

    if device["backup_status"] != "Successful":
        reasons.append("Backup failure")

    if device["uptime_days"] < 7:
        reasons.append("Low uptime")

    if device["status"] != "Operational":
        reasons.append("Non-operational status")

    return reasons


device_type_totals = {}
location_totals = {}
attention_devices = []

print("=" * 70)
print("NETWORK AUTOMATION OPERATIONAL REPORT")
print("=" * 70)

print(f"Total devices analyzed: {len(devices)}")

for device in devices:
    device_type = device["device_type"]
    location = device["location"]

    if device_type in device_type_totals:
        device_type_totals[device_type] += 1
    else:
        device_type_totals[device_type] = 1

    if location in location_totals:
        location_totals[location] += 1
    else:
        location_totals[location] = 1

    reasons = check_device(device)

    print("\n" + "-" * 70)
    print(f"Hostname:       {device['hostname']}")
    print(f"Device Type:    {device['device_type']}")
    print(f"Management IP:  {device['management_ip']}")
    print(f"Location:       {device['location']}")
    print(f"Status:         {device['status']}")
    print(f"CPU Usage:      {device['cpu_usage']}%")
    print(f"Memory Usage:   {device['memory_usage']}%")
    print(f"Uptime:         {device['uptime_days']} days")
    print(f"Backup Status:  {device['backup_status']}")

    if reasons:
        print(f"Attention:      YES - {', '.join(reasons)}")
        attention_devices.append(device["hostname"])
    else:
        print("Attention:      No")

print("\n" + "=" * 70)
print("DEVICE TYPE TOTALS")
print("=" * 70)

for device_type, total in device_type_totals.items():
    print(f"{device_type}: {total}")

print("\n" + "=" * 70)
print("LOCATION TOTALS")
print("=" * 70)

for location, total in location_totals.items():
    print(f"{location}: {total}")

print("\n" + "=" * 70)
print("DEVICES REQUIRING ATTENTION")
print("=" * 70)

print(f"Total devices requiring attention: {len(attention_devices)}")

for hostname in attention_devices:
    print(f"- {hostname}")