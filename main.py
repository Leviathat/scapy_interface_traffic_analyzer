
from common import protocol_counter, source_ip_counter, destination_ip_counter, packet_sizes
from analyzer import TrafficAnalyzerService
from visualization import VisualizationService

import threading
import time


if __name__ == "__main__":
    analyzer = TrafficAnalyzerService(iface='Ethernet', packet_count=100)
    
    sniffing_thread = threading.Thread(target=analyzer.start_sniffing)
    sniffing_thread.start()
    
    sniffing_thread.join()

    visualizer = VisualizationService()
    
    visualizer.plot_protocol_distribution()
    visualizer.plot_ip_distribution(source_ip_counter, 'Top 10 Source IP Addresses')
    visualizer.plot_ip_distribution(destination_ip_counter, 'Top 10 Destination IP Addresses')
    visualizer.plot_packet_size_distribution()
