import struct

class QUIC:

    def __init__(self, data):

        self.data = data

        first_byte = data[0]

        self.header_form = (first_byte & 0x80) >> 7

        self.packet_type = "Unknown"
        self.version = None

        if self.header_form:
            self.parse_long_header(data)
        else:
            self.parse_short_header(data)


    def parse_long_header(self,data):
        first_byte = data[0]

        packet_type_bits = (first_byte & 0x30) >> 4

        packet_types = {
            0: "Initial",
            1: "0-RTT",
            2: "Handshake",
            3: "Retry"
        }

        self.packet_type = packet_types.get(packet_type_bits,"Unknown")

        self.version = struct.unpack("!I", data[1:5])[0]

        offset = 5

        self.dest_conn_id_len = data[offset]
        offset += 1

        self.dest_conn_id = data[offset:offset+self.dest_conn_id_len]
        offset += self.dest_conn_id_len

        self.src_conn_id_len = data[offset]
        offset += 1

        self.src_conn_id = data[offset:offset+self.src_conn_id_len]

    def parse_short_header(self,data):

        self.packet_type = "Short Header"
        self.version = "N/A"