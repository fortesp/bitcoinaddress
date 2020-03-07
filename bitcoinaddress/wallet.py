from . import Address
from . import Key


class Wallet:

    def __init__(self, seed=None):
        self.key = Key(seed)
        self.address = Address(self.key)

    def __str__(self):
        return """%s\n%s""" % (self.key, self.address)
