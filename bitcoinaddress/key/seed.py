#  Bitcoin Address  v0.1
#  Copyright (c) 2020 - https://github.com/fortesp/bitcoinaddress
#  This software is distributed under the terms of the MIT License.
#  See the file 'LICENSE' in the root directory of the present distribution,
#  or http://opensource.org/licenses/MIT.

import time
from random import getrandbits
from mnemonic import Mnemonic


class Seed:

    def __init__(self, data=None, mnemonic=False):
        self.data = data
        self.mnemonic = mnemonic

    def generate(self):
        if self.mnemonic:  # TODO
            m = Mnemonic("english")
            if self.data is None:
                self.data = m.generate(strength=256)
        else:
            if self.data is None:
                self.data = Seed.random()

    @staticmethod
    def random():
        current_time = int(time.time())
        return str(getrandbits(30000) - current_time)

    def __str__(self):
        return self.data
