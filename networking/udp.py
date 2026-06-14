import struct


class UDP:

    def __init__(self, raw_data):
        self.src_port, self.dest_port, self.size = struct.unpack('! H H 2x H', raw_data[:8])
        self.data = raw_data[8:]

    def print(self, TABS):
        print(TABS[0] + 'UDP Segment:')
        print(TABS[1] + 'Source Port: {}, Destination Port: {}, Length: {}'.format(self.src_port, self.dest_port, self.size))