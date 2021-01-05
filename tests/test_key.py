import unittest
from unittest import TestCase

from bitcoinaddress import Key, Seed


class TestKey(TestCase):

    def testFromRandomSeed(self):
        # given
        key = Key.of(Seed())

        # then
        self.assertEqual(len(key.hex), 64)
        self.assertEqual(len(key.mainnet.wif), 51)
        self.assertEqual(len(key.mainnet.wifc), 52)

    def testFromHex_K(self):
        # given
        key = Key.of('669182eb2c3169e01cfc305034dc0b1df8328c274865e70d632c711ba62ec3d3')

        # then
        self.assertEqual(key.hex, '669182eb2c3169e01cfc305034dc0b1df8328c274865e70d632c711ba62ec3d3')
        self.assertEqual(key.mainnet.wif, '5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM')
        self.assertEqual(key.mainnet.wifc, 'Kzf6CYbTbBgoQEVXCWLVef1psFkoVjor7mxeyr2TDKWto7iHfXHh')

    def testFromHex_L(self):
        # given
        key = Key.of('c2814c56793485f803430ef28ea93ba34e1dc74a74cead43407378350a958792')

        # then
        self.assertEqual(key.hex, 'c2814c56793485f803430ef28ea93ba34e1dc74a74cead43407378350a958792')
        self.assertEqual(key.mainnet.wif, '5KHwxCT8Nrb3MSiQRS5h6fqmAJWrXzi9min15xSzY1EuR3EgLHT')
        self.assertEqual(key.mainnet.wifc, 'L3joYdYKZTsFPEVkNqhhz2SDv4JmdoidiPPdNsjiwr4NLr31PkqK')

    def testFromWIF(self):
        # given
        key = Key.of('5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM')

        # then
        self.assertEqual(key.hex, '669182eb2c3169e01cfc305034dc0b1df8328c274865e70d632c711ba62ec3d3')
        self.assertEqual(key.mainnet.wif, '5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM')
        self.assertEqual(key.mainnet.wifc, 'Kzf6CYbTbBgoQEVXCWLVef1psFkoVjor7mxeyr2TDKWto7iHfXHh')


if __name__ == "__main__":
    unittest.main()
