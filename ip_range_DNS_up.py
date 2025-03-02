import nmap
import socket
from tabulate import tabulate

# Define the IP range to scan
IP_RANGE = "10.10.0.0/16"

# Initialize the nmap scanner
scanner = nmap.PortScanner()

# Perform a ping scan to find live hosts
print("Scanning IP range for active hosts...")
scanner.scan(hosts=IP_RANGE, arguments="-sn")

# Initialize lists to hold data for both tables
ip_dns_table = []

for host in scanner.all_hosts():
    # Check if the host is up
    status = "Up" if scanner[host].state() == "up" else "Down"
    
    # Try to resolve DNS name
    try:
        dns_name = socket.gethostbyaddr(host)[0]
    except socket.herror:
        dns_name = "N/A"  # DNS lookup failed

    # Append data to the tables
    ip_dns_table.append([host, dns_name,status])

# Print tables
print("\nIP and DNS Table:")
print(tabulate(ip_dns_table, headers=["IP Address", "DNS Name","Status"], tablefmt="grid"))
