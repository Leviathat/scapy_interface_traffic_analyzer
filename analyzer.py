
from common import protocol_counter, source_ip_counter, destination_ip_counter, packet_sizes
from scapy.all import sniff, IP, TCP, UDP

class TrafficAnalyzerService:
    def __init__(self, iface='eth0', packet_count=100):
        self.iface = iface
        self.packet_count = packet_count

    def packet_callback(self, packet):
        if IP in packet:
            source_ip = packet[IP].src
            destination_ip = packet[IP].dst
            protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"

            protocol_counter[protocol] += 1
            source_ip_counter[source_ip] += 1
            destination_ip_counter[destination_ip] += 1
            packet_sizes.append(len(packet))

    def start_sniffing(self):
        print("Starting packet capture on interface:", self.iface)
        sniff(iface=self.iface, prn=self.packet_callback, count=self.packet_count)
        print("Packet capture completed.")