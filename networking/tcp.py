import struct
from general import *

class TCP:

    def __init__(self, raw_data):
        (self.src_port, self.dest_port, self.sequence, self.acknowledgment, offset_reserved_flags) = struct.unpack(
            '! H H L L H', raw_data[:14])
        offset = (offset_reserved_flags >> 12) * 4
        self.flag_urg = (offset_reserved_flags & 32) >> 5
        self.flag_ack = (offset_reserved_flags & 16) >> 4
        self.flag_psh = (offset_reserved_flags & 8) >> 3
        self.flag_rst = (offset_reserved_flags & 4) >> 2
        self.flag_syn = (offset_reserved_flags & 2) >> 1
        self.flag_fin = offset_reserved_flags & 1
        self.data = raw_data[offset:]

    def print(self, TABS):
        print(TABS[0] + 'TCP Segment:')
        print(TABS[1] + 'Source Port: {}, Destination Port: {}'.format(self.src_port, self.dest_port))
        print(TABS[1] + 'Sequence: {}, Acknowledgment: {}'.format(self.sequence, self.acknowledgment))
        print(TABS[1] + 'Flags:')
        print(TABS[2] + 'URG: {}, ACK: {}, PSH: {}'.format(self.flag_urg, self.flag_ack, self.flag_psh))
        print(TABS[2] + 'RST: {}, SYN: {}, FIN:{}'.format(self.flag_rst, self.flag_syn, self.flag_fin))

    def print_data(self, TABS,DATA_TABS):
        print(TABS[1] + 'TCP/HTTP Data:')
        print(format_multi_line(DATA_TABS[2], self.data))