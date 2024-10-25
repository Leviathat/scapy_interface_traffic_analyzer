from common import protocol_counter, source_ip_counter, destination_ip_counter, packet_sizes
import matplotlib.pyplot as plt

class VisualizationService:
    def plot_protocol_distribution(self):
        protocols = list(protocol_counter.keys())
        counts = list(protocol_counter.values())

        plt.figure(figsize=(8, 6))
        plt.bar(protocols, counts, color='skyblue')
        plt.xlabel('Protocol')
        plt.ylabel('Count')
        plt.title('Protocol Distribution')
        plt.show()

    def plot_ip_distribution(self, ip_counter, title):
        ip_addresses = list(ip_counter.keys())[:10]
        counts = list(ip_counter.values())[:10]

        plt.figure(figsize=(10, 6))
        plt.barh(ip_addresses, counts, color='lightgreen')
        plt.xlabel('Count')
        plt.ylabel('IP Address')
        plt.title(title)
        plt.gca().invert_yaxis()
        plt.show()

    def plot_packet_size_distribution(self):
        plt.figure(figsize=(10, 6))
        plt.hist(packet_sizes, bins=20, color='salmon', edgecolor='black')
        plt.xlabel('Packet Size (bytes)')
        plt.ylabel('Frequency')
        plt.title('Packet Size Distribution')
        plt.show()
