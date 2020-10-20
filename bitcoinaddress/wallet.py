#  Bitcoin Address  v0.1
#  Copyright (c) 2020 - https://github.com/fortesp/bitcoinaddress
#  This software is distributed under the terms of the MIT License.
#  See the file 'LICENSE' in the root directory of the present distribution,
#  or http://opensource.org/licenses/MIT.

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
