import re
class Parser:

    def __init__(self, data):
        self.data = data

    def parse(self):
        output = []
        for i in self.data.replace(b'[', b'').replace(b']', b'').replace(b'"', b'').split(b'\\n'):
            str_i = i.decode('utf-8')
            if re.match('^,(.*)', str_i):
                str_i = str_i.replace(',', '', 1)
            output.append(str_i.encode('utf-8') + b'\n')
        return output

