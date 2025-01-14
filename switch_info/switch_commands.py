commands_dic = {

    "nortell":  {
        # Get VLAN information
        "vlan_output" : "show vlan",
        # Get LLDP neighbors
        "lldp_output" : "show lldp neighbor detail"
    },

    "cisco" : {
        # Get VLAN information
        "vlan_output" : "show vlan-switch",
        # Get LLDP neighbors
        "lldp_output" : "show lldp neighbor detail"
    },

    "hp_procurve": {
        # Get VLAN information
        "vlan_output" : "show running-config",
        # Get LLDP neighbors
        "lldp_output" : "show cdp neighbors"
    }


}