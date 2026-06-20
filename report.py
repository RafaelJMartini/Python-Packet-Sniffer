class QUICStats:
    total = 0
    long_header = 0
    short_header = 0

    initial = 0
    handshake = 0
    zero_rtt = 0
    retry = 0

    @classmethod
    def update(cls, quic):

        cls.total += 1

        if quic.header_form:
            cls.long_header += 1
        else:
            cls.short_header += 1

        if quic.packet_type == "Initial":
            cls.initial += 1

        elif quic.packet_type == "Handshake":
            cls.handshake += 1

        elif quic.packet_type == "0-RTT":
            cls.zero_rtt += 1

        elif quic.packet_type == "Retry":
            cls.retry += 1

    @classmethod
    def save(cls):
        with open("quic_stats.txt", "w") as f:
            f.write("=== QUIC REPORT ===\n\n")
            f.write(f"Total QUIC: {cls.total}\n")
            f.write(f"Long Header: {cls.long_header} " + (f"({(cls.long_header/cls.total)*100:.2f}%)\n" if cls.total > 0 else ""))
            f.write(f"Short Header: {cls.short_header} " + (f"({(cls.short_header/cls.total)*100:.2f}%)\n" if cls.total > 0 else ""))
            f.write(f"Initial: {cls.initial}\n")
            f.write(f"Handshake: {cls.handshake}\n")
            f.write(f"0-RTT: {cls.zero_rtt}\n")
            f.write(f"Retry: {cls.retry}\n")