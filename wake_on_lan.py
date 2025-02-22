import socket
import struct
import argparse

def send_wol(mac_address, ip_address, port=9):
    # Convert MAC address to bytes
    mac_bytes = bytes.fromhex(mac_address.replace(':', '').replace('-', ''))
    
    # Construct magic packet
    magic_packet = b'\xff' * 6 + mac_bytes * 16
    
    # Create UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, (ip_address, port))
    print(f"WOL packet sent to {mac_address} via {ip_address}:{port}")

if __name__ == "__main__":

    mac  = "b0:22:7a:2f:53:87"
    ip   = "10.101.149.54"
    port = 9
    
    send_wol(mac, ip, port)
