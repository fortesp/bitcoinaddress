from . import Address
from . import Key


class Wallet:

    def __init__(self, seed=None):
        self.key = Key(seed)
        self.address = Address(self.key)

        self.key.generate()
        self.address.generate()

    def __str__(self):
        return """%s\n%s""" % (self.key, self.address)
