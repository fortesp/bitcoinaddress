import hashlib
import random
import time

import base58

from .util import doublehash256


class Key:

    def __init__(self, seed=None):
        self.hash = ''
        self.hashdigest = ''
        self.hex = ''
        self.wif = ''
        self.wif_c = ''

    def _seed(self):
        t = int(time.time())
        return str(random.getrandbits(3000) - t)

    def generate(self, seed=None):
        self._generate_raw(seed)
        self._generate_hex()
        self._generate_wif()

        return {'hex': self.hex, 'wif': self.wif, 'wifc': self.wif_c}

    def _generate_raw(self, seed=None):
        if (seed == None): seed = self._seed()
        self.hash = hashlib.sha256(seed.encode())
        self.hashdigest = self.hash.digest()

    def _generate_hex(self):
        self.hex = self.hash.hexdigest()

    def _generate_wif(self):
        prefix = b'\x80'
        suffix = b'\x01'

        d = prefix + self.hashdigest

        checksum = doublehash256(d).digest()[:4]
        checksum_c = doublehash256(d + suffix).digest()[:4]

        self.wif = base58.b58encode(d + checksum).decode('utf-8')
        self.wif_c = base58.b58encode(d + suffix + checksum_c).decode('utf-8')

    def __str__(self):
        return """Private Key HEX: %s
                \rPrivate Key WIF: %s\r
                \rPrivate Key WIF compressed: %s 
                """ % (self.hex, self.wif, self.wif_c)
