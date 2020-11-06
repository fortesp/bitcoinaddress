from binascii import hexlify
from random import getrandbits
from mnemonic import Mnemonic
import time

class Seed:

    def __init__(self, data=None, mnemonic=False):
        if mnemonic:
            m = Mnemonic("english")
            if data is None:
                self.data = m.generate(strength=256)
            else:
                self.data = m.to_seed(data, passphrase="")
        else:
            if data is None:
                self.data = Seed.random()

    @staticmethod
    def random():
        current_time = int(time.time())
        return str(getrandbits(30000) - current_time)

    def __str__(self):
        return hexlify(self.data).decode()
