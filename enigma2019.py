letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
let = {i:letters[i] for i in range(26)}
num = {let[i]:i for i in range(26)}
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


class enigma (object):
    def __init__(self, rotors, rin, ref, plg):
        self.notches = [num[rotors[i][1]] for i in range(len(rotors))]
        self.rings = [num[x] for x in rin]

        self.r0 = {i: num[rot[0][0][i]] for i in range(26)}
        self.r1 = {i: num[rot[1][0][i]] for i in range(26)}
        self.r2 = {i: num[rot[2][0][i]] for i in range(26)}
        self.r0i = {y: x for x, y in self.r0.items()}
        self.r1i = {y: x for x, y in self.r1.items()}
        self.r2i = {y: x for x, y in self.r2.items()}
        self.r = {i: num[ref[i]] for i in range(26)}
        self.pb = {i: i for i in range(26)}
        for x in plg:
            self.pb[num[x[0]]], self.pb[num[x[1]]] = self.pb[num[x[1]]], self.pb[num[x[0]]]

        self.r0 = [self.r0[i] for i in range(26)]
        self.r1 = [self.r1[i] for i in range(26)]
        self.r2 = [self.r2[i] for i in range(26)]
        self.r0i = [self.r0i[i] for i in range(26)]
        self.r1i = [self.r1i[i] for i in range(26)]
        self.r2i = [self.r2i[i] for i in range(26)]
        self.r = [self.r[i] for i in range(26)]
        self.pb = [self.pb[i] for i in range(26)]

    def rotorstep(self, posit):
        out = posit
        # DOES NOT WORK FOR MULTIPLE NOTCHES
        if out[1] == self.notches[1]:
            out[0] = (out[0] + 1) % 26
            out[1] = (out[1] + 1) % 26
        if out[2] == self.notches[2]:
            out[1] = (out[1] + 1) % 26
        out[2] = (out[2] + 1) % 26
        return out
    def decrypt(self, pos, ciphertext):
        plaintext = []
        posn = [num[i] for i in pos]
        ciphertext = [self.pb[num[i]] for i in ciphertext]
        for i in ciphertext:
            posn = self.rotorstep(posn)
            a, b, c = posn[0] - self.rings[0], posn[1] - self.rings[1], posn[2] - self.rings[2]
            out = i
            out = self.r2[(out + c) % 26] - c
            out = self.r1[(out + b) % 26] - b
            out = self.r0[(out + a) % 26] - a
            out = self.r[out % 26]
            out = self.r0i[(out + a) % 26] - a
            out = self.r1i[(out + b) % 26] - b
            out = self.r2i[(out + c) % 26] - c
            plaintext.append(out)
        plaintext = [let[self.pb[i % 26]] for i in plaintext]
        return ''.join(plaintext)


rot = [rII, rI, rIII]
rin = ['J', 'G', 'N']
ref = rB
plg = ['NK', 'ER', 'AY', 'TJ', 'CB', 'QM', 'SL', 'WO', 'IG', 'FH']
enig = enigma(rot, rin, ref, plg)

pos = ['Y', 'Y', 'E']
inpt = 'QATCTQCNWMTVCOPYVFHOLCQTVGMTWOBRFOUBRMQBRIHLLXDBTZLXLGZUQFCWPXPOKOLFFADXDAVTJM'
print(enig.decrypt(pos, inpt))

import time
inpt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inpt = inpt * 10000
t = time.clock()
outpt = enig.decrypt(pos, inpt)
print(len(inpt)/(time.clock() - t))
