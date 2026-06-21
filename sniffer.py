import socket
from general import *
from networking.ethernet import Ethernet
from networking.ipv4 import IPv4
from networking.icmp import ICMP
from networking.tcp import TCP
from networking.udp import UDP
from networking.pcap import Pcap
from networking.http import HTTP
from networking.quic import QUIC
from report import QUICStats

TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '
TABS = [TAB_1,TAB_2,TAB_3,TAB_4]

DATA_TAB_1 = '\t   '
DATA_TAB_2 = '\t\t   '
DATA_TAB_3 = '\t\t\t   '
DATA_TAB_4 = '\t\t\t\t   '
DATA_TABS = [DATA_TAB_1,DATA_TAB_2,DATA_TAB_3,DATA_TAB_4]


def main():
    pcap = Pcap('capture.pcap')
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        raw_data, addr = conn.recvfrom(65535)
        pcap.write(raw_data)
        eth = Ethernet(raw_data)
        eth.print(TABS)

        # IPv4
        if eth.proto == 8:
            ipv4 = IPv4(eth.data)
            ipv4.print(TABS)

            # ICMP
            if ipv4.proto == 1:
                icmp = ICMP(ipv4.data)
                icmp.print(TABS, DATA_TABS)


                # TCP
            elif ipv4.proto == 6:
                tcp = TCP(ipv4.data)
                tcp.print(TABS)

                if len(tcp.data) > 0:

                    # HTTP
                    if tcp.src_port == 80 or tcp.dest_port == 80:

                        print(TABS[1] + 'HTTP Data:')
                        try:
                            http = HTTP(tcp.data)
                            http.print(TABS)
                        except:
                            tcp.print_data(TABS,DATA_TABS)

                    else:
                        tcp.print_data(TABS,DATA_TABS)

            # UDP
            elif ipv4.proto == 17:
                udp = UDP(ipv4.data)
                udp.print(TABS)
                
                # QUIC
                if udp.src_port == 443 or udp.dest_port == 443:
                    first_byte = udp.data[0]
                    fixed_bit = (first_byte & 0x40) >> 6
                    if fixed_bit != 1:
                        print(TAB_2 + 'Not QUIC (invalid fixed bit)')
                        continue
                    quic = QUIC(udp.data)

                    QUICStats.update(quic)
                    QUICStats.save()
                    
                    quic.print(TABS)

            # Other IPv4
            else:
                print(TAB_1 + 'Other IPv4 Data:')
                print(format_multi_line(DATA_TAB_2, ipv4.data))

        else:
            print('Ethernet Data:')
            print(format_multi_line(DATA_TAB_1, eth.data))

    pcap.close()


main()
