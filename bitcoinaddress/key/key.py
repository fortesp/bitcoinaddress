#  Bitcoin Address  v0.1
#  Copyright (c) 2020 - https://github.com/fortesp/bitcoinaddress
#  This software is distributed under the terms of the MIT License.
#  See the file 'LICENSE' in the root directory of the present distribution,
#  or http://opensource.org/licenses/MIT.

import hashlib
import base58
from binascii import hexlify, unhexlify
from .seed import Seed
from bitcoinaddress.util import doublehash256


class Key:

    CHECKSUM_SIZE = 4

    def __init__(self, seed=None):
        self.seed = seed
        self.digest = None
        self.hex = None
        self.wif = None
        self.wif_c = None
        self.wif_testnet = None
        self.wif_c_testnet = None

    def generate_from_hex(self, hex):
        self.digest = unhexlify(hex)

        self._generate_hex()
        self._generate_wif()
        self._generate_wif_testnet()
        return self.__return()

    def generate_from_wif(self, wif):
        self.digest = self.__wif_to_digest(wif)

        self._generate_hex()
        self._generate_wif()
        self._generate_wif_testnet()
        return self.__return()

    def generate(self):
        self._generate_digest()
        self._generate_hex()
        self._generate_wif()
        self._generate_wif_testnet()
        return self.__return()

    def _generate_digest(self):
        if self.seed is None:
            self.seed = Seed.random()
        else:
            if isinstance(self.seed, Seed):
                self.seed = str(self.seed.data)

        hash = hashlib.sha256(self.seed.encode())
        self.digest = hash.digest()

    def _generate_hex(self):
        self.hex = hexlify(self.digest).decode()

    def _generate_wif(self):
        prefix = b'\x80'
        suffix = b'\x01'
        self.wif, self.wif_c = self.__generate_wif(prefix, suffix)

    def _generate_wif_testnet(self):
        prefix = b'\xEF'
        suffix = b'\x01'
        self.wif_testnet, self.wif_c_testnet = self.__generate_wif(prefix, suffix)

    def __generate_wif(self, prefix, suffix):
        _digest = prefix + self.digest

        checksum = doublehash256(_digest).digest()[:Key.CHECKSUM_SIZE]
        checksum_c = doublehash256(_digest + suffix).digest()[:Key.CHECKSUM_SIZE]

        wif = base58.b58encode(_digest + checksum).decode('utf-8')
        wif_c = base58.b58encode(_digest + suffix + checksum_c).decode('utf-8')
        return wif, wif_c

    def __wif_to_digest(self, wif):
        return base58.b58decode(wif)[1:-Key.CHECKSUM_SIZE]

    def __return(self):
        return {'hex': self.hex, 'wif': self.wif, 'wifc': self.wif_c,
                'testnet': {'hex': self.hex, 'wif': self.wif_testnet, 'wifc': self.wif_c_testnet}}

    def __str__(self):
        return """Private Key HEX: %s\n
                \rPrivate Key WIF: %s
                \rPrivate Key WIF compressed: %s
                \rPrivate Key WIF (TESTNET): %s
                \rPrivate Key WIF compressed (TESTNET): %s 
                """ % (self.hex, self.wif, self.wif_c, self.wif_testnet, self.wif_c_testnet)
