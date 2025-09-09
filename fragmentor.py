#!/usr/bin/env python3
import argparse, random
import scapy
from scapy.all import conf
# This line is crucial for avoiding the raw socket error
# by telling scapy not to use a Layer 3 socket.
conf.L3socket = None
from scapy.layers.inet import IP, TCP, fragment
from scapy.packet import Raw
from scapy.utils import RawPcapWriter

def build_request(host, path, body):
    """
    Builds the complete HTTP POST request string.
    """
    req = (
        f"POST {path} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Connection: close\r\n\r\n"
        f"{body}"
    )
    return req.encode()

def fragment_packet(dst, port, payload, fragsize):
    """
    Fragments the payload into multiple IP packets.
    """
    ip_id = random.randint(1, 65535)
    ip = IP(dst=dst, id=ip_id)
    tcp = TCP(sport=random.randint(1024, 65535), dport=port, flags="PA", seq=1000)
    pkt = ip / tcp / Raw(payload)
    return fragment(pkt, fragsize)

def main():
    """
    Main function to parse arguments and create fragmented packets for each command.
    """
    parser = argparse.ArgumentParser(description="Multi-command HTTP fragmenter for THM lab")
    parser.add_argument("--dst", required=True)
    parser.add_argument("--port", type=int, default=80)
    parser.add_argument("--host", required=True)
    parser.add_argument("--path", default="/")
    parser.add_argument("--commands", nargs="+", required=True)
    parser.add_argument("--fragsize", type=int, default=100)
    args = parser.parse_args()

    for idx, cmd in enumerate(args.commands, 1):
        print(f"[*] Building fragments for command {idx}: {cmd}")
        # Build the full HTTP request body
        req = build_request(args.host, args.path, cmd)
        # Fragment the packet based on the specified fragment size
        frags = fragment_packet(args.dst, args.port, req, args.fragsize)
        # Define the output filename for the PCAP
        outname = f"frag_cmd{idx}.pcap"
        # Write the fragmented packets to the PCAP file
        writer = RawPcapWriter(outname, linktype=1)
        for f in frags:
            writer.write(f)
        print(f"    -> Saved {len(frags)} fragments to {outname}")

if __name__ == "__main__":
    main()