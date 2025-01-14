from netmiko import ConnectHandler
from netmiko import ConnectHandler
from netmiko.exceptions import SSHException
from paramiko.ssh_exception import SSHException as ParamikoSSHException
from switch_info_dic import switch_LIST
from switch_commands import commands_dic

def get_vlan_and_lldp_info(switch):
    
    try:
        # Increase SSH timeout
        connection = ConnectHandler(**switch, banner_timeout=30)

        # Enter enable mode if necessary
        if switch.get("secret"):
            connection.enable()

        vlan_command, lldp_command = get_commands(switch["device_type"])

        # Get VLAN information
        vlan_output = connection.send_command(vlan_command)

        # Get LLDP neighbors
        lldp_output = connection.send_command(lldp_command)

        # Close the connection
        connection.disconnect()

        return vlan_output, lldp_output
    except Exception as e:
        print(f"Failed with for switch {switch['host']}: {e}")

    print(f"All device types failed for switch {switch['host']}")
    return None, None



def get_commands (device_type:str):

    cisco_device_types = ["cisco_ios","cisco_ios_telnet"]
    nortell_device_types = ["avaya_ers"]
    hp_procurve = ["hp_procurve_telnet"]

    if device_type in cisco_device_types:
        command_type = "cisco"
    elif device_type in hp_procurve:
        command_type = "hp_procurve"
    elif device_type in nortell_device_types:
        command_type = "nortell"
    else:
        return None

    return (commands_dic[command_type]["vlan_output"], commands_dic[command_type]["lldp_output"])


def verify_connection(switch):

    try:
        # Increase SSH timeout
        connection = ConnectHandler(**switch, banner_timeout=30)
        print(f"Sucessfull conection with switch {switch['host']}")
    except Exception as e:
        print(f"Failed with for switch {switch['host']}: {e}")

# Main function
if __name__ == "__main__":
    for switch in switch_LIST:
        print(f"\nConnecting to switch: {switch['host']}")
        vlan_info, lldp_info = get_vlan_and_lldp_info(switch)
        #verify_connection(switch)
        if vlan_info and lldp_info:
            info_string =" "
            info_string += f"\n--- VLAN Information for {switch['host']} ---\n"
            info_string += vlan_info
            info_string += f"\n--- LLDP Neighbors for {switch['host']} ---\n"
            info_string += lldp_info

            with open(f"switch_info/{switch['host']}.txt", "w") as f:
                f.write(info_string)

        else:
            print(f"Failed to retrieve information for switch {switch['host']}")