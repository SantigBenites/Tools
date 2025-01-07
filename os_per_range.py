import nmap

def scan_os(ip_range):
    scanner = nmap.PortScanner()

    try:
        print(f"Scanning IP range: {ip_range} for OS detection...")
        scanner.scan(hosts=ip_range, arguments='-O')  # '-O' enables OS detection

        for host in scanner.all_hosts():
            print(f"\nHost: {host}")
            print(f"State: {scanner[host].state()}")

            if 'osmatch' in scanner[host]:
                os_matches = scanner[host]['osmatch']
                if os_matches:
                    print("Possible OS:")
                    for os_match in os_matches:
                        print(f"  - {os_match['name']} (accuracy: {os_match['accuracy']}%)")
                else:
                    print("No OS matches found.")
            else:
                print("OS detection not available for this host.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ip_range = "10.101.84.0/25"
    scan_os(ip_range)