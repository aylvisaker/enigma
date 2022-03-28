class Text:
    # todo basic statistics: frequencies, ic, ngrams
    def __init__(self, text=None, numeric=None):
        self.numeric = numeric
        self.text = text
        if text:
            self.update_numeric()
        elif numeric:
            self.update_text()

    def update_text(self):
        self.text = ''.join(HistoricalConstants.numeric_to_alpha[n] for n in self.numeric)

    def update_numeric(self):
        self.numeric = (HistoricalConstants.alpha_to_numeric[t] for t in self.text)


class MachineComponent:
    def __init__(self, permutation: dict, left_neighbor=None, right_neighbor=None):
        self.permutation = permutation
        self.inverse = {x: y for y, x in permutation.items()}
        self._left_neighbor = left_neighbor
        self._right_neighbor = right_neighbor

    def forward_map(self, key):
        if key in self.permutation:
            return self.permutation[key]
        else:
            return key

    def reverse_map(self, key):
        if key in self.inverse:
            return self.inverse[key]
        else:
            return key


class Plugboard(MachineComponent):
    def __init__(self, permutation, left_neighbor=None, right_neighbor=None):
        super().__init__(permutation, left_neighbor, right_neighbor)


class Rotor(MachineComponent):
    # todo dictionaries for maps in various positions OR use modular arithmetic
    def __init__(self, permutation, left_neighbor=None, right_neighbor=None, position=0):
        super().__init__(permutation, left_neighbor, right_neighbor)
        self._position = position

    def step_forward(self):
        pass

    def step_to(self, position):
        self._position = position


class Reflector(MachineComponent):
    def __init__(self, permutation, left_neighbor=None, right_neighbor=None):
        super().__init__(permutation, left_neighbor, right_neighbor)


class Enigma:
    def __init__(self, components, settings):
        self.components = components  # plugboard, 3-4 rotors, reflector
        self.settings = settings  # rotor / ring positions

    def step_forward(self):
        pass

    def press(self, keypress):
        pass

    def copy(self):
        return Enigma(self.components, self.settings)


class Bombe:
    def __init__(self, ciphertext, plaintext):
        self._ciphertext = ciphertext
        self._plaintext = plaintext

    def try_pair(self, x, y):
        # multithreading search for contradiction if found return False
        # (enigma_object for each character in _ciphertext)
        pass

    def search(self):
        pass


class HistoricalConstants:
    rI = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q']
    rII = ['AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E']
    rIII = ['BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V']
    rIV = ['ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J']
    rV = ['VZBRGITYUPSDNHLXAWMJQOFECK', 'Z']
    rVI = ['JPGVOUMFYQBENHZRDKASXLICTW', 'ZM']
    rVII = ['NZJHGRCXMYSWBOUFAIVLPEKQDT', 'ZM']
    rVIII = ['FKQHTLXOCBJSPDZRAMEWNIUYGV', 'ZM']
    rA = 'EJMZALYXVBWFCRQUONTSPIKHGD'
    rB = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
    rC = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
    rBt = 'ENKQAUYWJICOPBLMDXZVFTHRGS'
    rCt = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_to_numeric = {a: b for a, b in enumerate(alphabet)}
    numeric_to_alpha = {b: a for a, b in enumerate(alphabet)}
