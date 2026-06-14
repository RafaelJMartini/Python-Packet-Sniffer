class QUIC:

    def __init__(self, data):

        self.data = data

        first_byte = data[0]

        self.header_form = (first_byte & 0x80) >> 7

        if self.header_form:
            self.parse_long_header(data)
        else:
            self.parse_short_header(data)