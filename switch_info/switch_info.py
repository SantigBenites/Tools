from netmiko import ConnectHandler
from switch_info_dic import AP_LIST

# Function to get VLANs and LLDP info from a switch
def get_vlan_lldp_info(device):
    for connection_type in ["ssh", "telnet"]:
        try:
            device["device_type"] = f"{device['device_type']}_{connection_type}"

            # Establish connection
            connection = ConnectHandler(**device)
            connection.enable()

            # Get VLAN information
            vlan_output = connection.send_command("show vlan brief")

            # Get LLDP neighbor information
            lldp_output = connection.send_command("show lldp neighbors detail")

            # Close the connection
            connection.disconnect()

            return vlan_output, lldp_output
        except Exception as e:
            print(f"Error connecting to {device['host']} via {connection_type}: {e}")

    print(f"Failed to connect to {device['host']} via both SSH and Telnet.")
    return None, None

# Main script
if __name__ == "__main__":
    for ap in AP_LIST:
        print(f"\nQuerying AP: {ap['host']}\n")
        vlan_info, lldp_info = get_vlan_lldp_info(ap)

        if vlan_info and lldp_info:
            print("--- VLAN Information ---")
            print(vlan_info)

            print("\n--- LLDP Information ---")
            print(lldp_info)
        else:
            print("Failed to retrieve information from this AP.")