class Text:
    # todo extend to_numeric and add default value
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_to_numeric = {a: b for a, b in enumerate(alphabet)}
    numeric_to_alpha = {b: a for a, b in enumerate(alphabet)}

    def __init__(self, text):
        # initialize with numeric only
        self._numeric = None
        self._text = text
        self.update_numeric()

    def update_text(self):
        self._text = ''.join(self.numeric_to_alpha[n] for n in self._numeric)

    def update_numeric(self):
        self._numeric = (self.alpha_to_numeric[t] for t in self._text)


class MachineComponent:
    def __init__(self, mapping, left_neighbor=None, right_neighbor=None):
        self._map = mapping
        self._inverse_map = {}
        self._left_neighbor = left_neighbor
        self._right_neighbor = right_neighbor

    def forward_map(self, key):
        if not key:
            pass
        return self._map[key]

    def reverse_map(self, light):
        return self._map[light]


class Plugboard(MachineComponent):
    pass


class Rotor(MachineComponent):
    # todo dictionaries for maps in various positions OR use modular arithmetic
    def __init__(self, mapping, left_neighbor=None, right_neighbor=None, position=0):
        super().__init__(mapping, left_neighbor, right_neighbor)
        self._position = position

    def step_forward(self):
        pass

    def step_to(self):
        pass


class Reflector(MachineComponent):
    pass


class Enigma:
    pass
    # plugboard, 3-4 rotors, reflector
    # rotor / ring positions
    # step method
    # press method
    # copy method


class Bombe:
    def __init__(self, ciphertext, plaintext):
        self._ciphertext = ciphertext
        self._plaintext = plaintext

    def try_pair(self, x, y):
        # multithreading search for contradiction
        # (enigma_object for each character in _ciphertext)
        pass

