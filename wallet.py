import binascii
import hashlib
import random
import time
import base58
import ecdsa

import segwit_addr

""" Bitcoin Wallet Generator v0.3

         Pedro Fortes - 05/2018
         Pedro Fortes - 01/2020 - Bech32 implementation

         https://bitcoincore.org/en/segwit_wallet_dev/
         https://pypi.python.org/pypi/ecdsa - ECDSA manual
         https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki#Reference_implementations - BIP 173
         """


class Keys:

    def __init__(self):
        self.privkeyhex = ''
        self.privkeywif = ''
        self.privkeywifcompressed = ''

        self.pubkey = ''
        self.pubkeycompressed = ''
        self.pubaddr1 = ''
        self.pubaddr3 = ''
        self.pubaddrbc1_P2WPKH = ''
        self.pubaddrbc1_P2WSH = ''

    def seed(self):
        t = int(time.time())
        return str(random.getrandbits(3000) - t)

    def privatekey(self, seed=None):
        if (seed == None): seed = self.seed()
        self.privkeyhex = hashlib.sha256(seed.encode())

    def privatekeywif(self):
        prefix = b'\x80'
        suffix = b'\x01'

        d = prefix + self.privkeyhex.digest()

        checksum = self.doublehash256(d).digest()[:4]
        checksum_c = self.doublehash256(d + suffix).digest()[:4]

        self.privkeywif = base58.b58encode(d + checksum).decode('utf-8')
        self.privkeywifcompressed = base58.b58encode(d + suffix + checksum_c).decode('utf-8')

    def hash160(self, v):
        r = hashlib.new('ripemd160')
        r.update(hashlib.sha256(v).digest())
        return r

    def doublehash256(self, v):
        return hashlib.sha256(hashlib.sha256(v).digest())

    def ecdsaSECP256k1(self, digest):
        # SECP256k1 - Bitcoin elliptic curve
        sk = ecdsa.SigningKey.from_string(digest, curve=ecdsa.SECP256k1)
        return sk.get_verifying_key()

    def publicaddress1(self):
        prefix_a = b'\x04'
        prefix_b = b'\x00'

        digest = self.privkeyhex.digest()

        p = prefix_a + self.ecdsaSECP256k1(digest).to_string()  # 1 + 32 bytes + 32 bytes
        self.pubkey = str(binascii.hexlify(p).decode('utf-8'))

        hash160 = self.hash160(p)

        m = prefix_b + hash160.digest()
        checksum = self.doublehash256(m).digest()[:4]

        self.pubaddr1 = base58.b58encode(m + checksum).decode('utf-8')

    def _generate_publickey(self):
        prefix_even = b'\x02'
        prefix_odd = b'\x03'
        prefix_a = prefix_odd

        digest = self.privkeyhex.digest()

        ecdsa_digest = self.ecdsaSECP256k1(digest).to_string()

        x_coord = ecdsa_digest[:int(len(ecdsa_digest) / 2)]
        y_coord = ecdsa_digest[int(len(ecdsa_digest) / 2):]

        if (int(binascii.hexlify(y_coord), 16) % 2 == 0): prefix_a = prefix_even

        p = prefix_a + x_coord

        self.pubkeycompressed = str(binascii.hexlify(p).decode('utf-8'))

        return p

    def publicaddress3(self):
        p = self._generate_publickey()

        prefix_redeem = b'\x00\x14'
        prefix_b = b'\x05'

        redeem_script = self.hash160(prefix_redeem + self.hash160(p).digest()).digest()  # 20 bytes

        m = prefix_b + redeem_script
        checksum = self.doublehash256(m).digest()[:4]

        self.pubaddr3 = base58.b58encode(m + checksum).decode('utf-8')

    def publicaddressbc1(self):
        p = self._generate_publickey()

        redeem_script_P2WPKH = self.hash160(p).digest()  # 20 bytes
        redeem_script_P2WSH = hashlib.sha256(p).digest()

        self.pubaddrbc1_P2WPKH = str(segwit_addr.encode('bc', 0x00, redeem_script_P2WPKH))
        self.pubaddrbc1_P2WSH = str(segwit_addr.encode('bc', 0x00, redeem_script_P2WSH))

    def generate(self, seed=None):
        self.privatekey(seed)
        self.privatekeywif()

        self.publicaddress1()
        self.publicaddress3()
        self.publicaddressbc1()

    def __str__(self):
        return """
Private Key HEX: %s
Private Key WIF: %s
Private Key WIF compressed: %s

Public Key: %s
Public Key compressed: %s

Public Address 1: %s
Public Address 3: %s
Public Address bc1 (P2WPKH): %s 
Public Address bc1 (P2WSH): %s
""" % (self.privkeyhex.hexdigest(), self.privkeywif, self.privkeywifcompressed, self.pubkey,
       self.pubkeycompressed, self.pubaddr1, self.pubaddr3, self.pubaddrbc1_P2WPKH, self.pubaddrbc1_P2WSH)


if __name__ == "__main__":
    wallet = Keys()
    wallet.generate()

    print(wallet)
