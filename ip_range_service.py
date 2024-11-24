import nmap
import ipaddress
import openpyxl
from openpyxl import Workbook

# Define the IP range and ports to scan
IP_RANGE = "10.101.84.128/25"
PORTS = "1-1000"  # Scan the first 1000 ports

# Initialize the nmap scanner
scanner = nmap.PortScanner()

# Get all IPs in the specified range
network = ipaddress.IPv4Network(IP_RANGE)

# Create a new Excel workbook and add a worksheet
wb = Workbook()
ws = wb.active
ws.title = "Scan Results"

# Write header row with host and port columns
header = ["Host"] + [f"Port {port}" for port in range(1, 1001)]
ws.append(header)

# Loop through each host in the IP range and scan specified ports
for ip in network.hosts():
    host = str(ip)  # Convert IP to string
    print(f"Scanning {host}...")

    # Scan the first 1000 ports for open/closed status
    scanner.scan(host, PORTS)
    
    # Prepare row data
    row = [host]  # Start a new row with the host's IP

    # Check if the host was successfully scanned
    if host in scanner.all_hosts() and scanner[host].state() == "up":
        # For each port, record "Open" if the port is open, otherwise "Closed"
        for port in range(1, 1001):
            if 'tcp' in scanner[host] and port in scanner[host]['tcp']:
                if scanner[host]['tcp'][port]['state'] == "open":
                    row.append("Open")
                else:
                    row.append("Closed")
            else:
                row.append("Closed")
    else:
        # If the host was not in the scan result, mark as "No Response" for all ports
        row.extend(["No Response"] * 1000)

    # Append row to the Excel sheet
    ws.append(row)

# Save the workbook to a file
output_file = "scan_results.xlsx"
wb.save(output_file)

print(f"\nScan completed. Results saved to {output_file}")
