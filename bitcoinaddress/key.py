#  Bitcoin Address  v0.1
#  Copyright (c) 2020 - https://github.com/fortesp/bitcoinaddress
#  This software is distributed under the terms of the MIT License.
#  See the file 'LICENSE' in the root directory of the present distribution,
#  or http://opensource.org/licenses/MIT.

import hashlib
import base58

from .util import doublehash256, randomseed


class Key:

    def __init__(self, seed=None):
        self.seed = seed
        self.hash = None
        self.hashdigest = None
        self.hex = None
        self.wif = None
        self.wif_c = None
        self.wif_testnet = None
        self.wif_c_testnet = None

    def generate(self):
        self._generate_raw(self.seed)
        self._generate_hex()
        self._generate_wif()
        self._generate_wif_testnet()

        return {'hex': self.hex, 'wif': self.wif, 'wifc': self.wif_c,
                'testnet': {'hex': self.hex, 'wif': self.wif_testnet, 'wifc': self.wif_c_testnet}}

    def _generate_raw(self, seed=None):
        if seed is None: seed = randomseed()
        self.hash = hashlib.sha256(seed.encode())
        self.hashdigest = self.hash.digest()

    def _generate_hex(self):
        self.hex = self.hash.hexdigest()

    def _generate_wif(self):
        prefix = b'\x80'
        suffix = b'\x01'

        _digest = prefix + self.hashdigest

        checksum = doublehash256(_digest).digest()[:4]
        checksum_c = doublehash256(_digest + suffix).digest()[:4]

        self.wif = base58.b58encode(_digest + checksum).decode('utf-8')
        self.wif_c = base58.b58encode(_digest + suffix + checksum_c).decode('utf-8')

    def _generate_wif_testnet(self):
        prefix = b'\xEF'
        suffix = b'\x01'

        _digest = prefix + self.hashdigest

        checksum = doublehash256(_digest).digest()[:4]
        checksum_c = doublehash256(_digest + suffix).digest()[:4]

        self.wif_testnet = base58.b58encode(_digest + checksum).decode('utf-8')
        self.wif_c_testnet = base58.b58encode(_digest + suffix + checksum_c).decode('utf-8')

    def __str__(self):
        return """Private Key HEX: %s\n
                \rPrivate Key WIF: %s
                \rPrivate Key WIF compressed: %s
                \rPrivate Key WIF (TESTNET): %s
                \rPrivate Key WIF compressed (TESTNET): %s 
                """ % (self.hex, self.wif, self.wif_c, self.wif_testnet, self.wif_c_testnet)
