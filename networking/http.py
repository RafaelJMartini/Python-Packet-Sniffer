

class HTTP:

    def __init__(self, raw_data):
        try:
            self.data = raw_data.decode('utf-8')
        except:
            self.data = raw_data

    def print(self, TABS, DATA_TABS):
        print(TABS[1] + 'HTTP Data:')
        http_info = str(self.data).split('\n')
        for line in http_info:
            print(DATA_TABS[2] + str(line))