import struct
from general import *

class ICMP:

    def __init__(self, raw_data):
        self.type, self.code, self.checksum = struct.unpack('! B B H', raw_data[:4])
        self.data = raw_data[4:]

    def print(self,TABS,DATA_TABS):
        print(TABS[0] + 'ICMP Packet:')
        print(TABS[1] + 'Type: {}, Code: {}, Checksum: {},'.format(self.type, self.code, self.checksum))
        print(TABS[1] + 'ICMP Data:')
        print(format_multi_line(DATA_TABS[2], self.data))