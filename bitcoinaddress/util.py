#  Bitcoin Address  v0.1
#  Copyright (c) 2020 - https://github.com/fortesp/bitcoinaddress
#  This software is distributed under the terms of the MIT License.
#  See the file 'LICENSE' in the root directory of the present distribution,
#  or http://opensource.org/licenses/MIT.

import hashlib
import time
import random
import ecdsa


def doublehash256(v):
    return hashlib.sha256(hashlib.sha256(v).digest())


def hash160(v):
    r = hashlib.new('ripemd160')
    r.update(hashlib.sha256(v).digest())
    return r


def ecdsa_secp256k1(digest):
    # SECP256k1 - Bitcoin elliptic curve
    sk = ecdsa.SigningKey.from_string(digest, curve=ecdsa.SECP256k1)
    return sk.get_verifying_key()


def randomseed():
    current_time = int(time.time())
    return str(random.getrandbits(3000) - current_time)
