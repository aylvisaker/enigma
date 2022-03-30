import string


class CipherText:
    def __init__(self, string):
        self.text = string

    def __str__(self):
        self.strip()
        out = ''
        text = self.text
        while text:
            out += text[:5] + ' '
            text = text[5:]
        return out.strip()

    def __len__(self):
        self.strip()
        return len(self.text)

    def strip(self):
        out = ''
        for c in self.text:
            if c in string.ascii_letters:
                out += c
        self.text = out.upper()

    def frequencies(self):
        n = len(self)
        d = {}
        for c in string.ascii_uppercase:
            d[c] = self.text.count(c) / n
        return d

    def index_of_coincidence(self):
        d = self.frequencies()


message = CipherText('THEQUICKBROWNFOXJUMPSOVERTHELAZYhotdog.')
message.strip()
print(str(message) + 'the'[5:])
print(message.text)
print(1//2)
print(1/2)