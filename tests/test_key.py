import unittest
from unittest import TestCase

from bitcoinaddress import Key


class TestKey(TestCase):

    def test_generate_from_hex(self):
        # given
        key = Key()
        key.generate_from_hex('669182eb2c3169e01cfc305034dc0b1df8328c274865e70d632c711ba62ec3d3')

        # then
        self.assertEqual(key.hex, '669182eb2c3169e01cfc305034dc0b1df8328c274865e70d632c711ba62ec3d3')
        self.assertEqual(key.wif, '5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM')
        self.assertEqual(key.wif_c, 'Kzf6CYbTbBgoQEVXCWLVef1psFkoVjor7mxeyr2TDKWto7iHfXHh')

    def test_generate_from_wif(self):
        # given
        key = Key()
        key.generate_from_wif('5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM')

        # then
        self.assertEqual(key.hex, '669182eb2c3169e01cfc305034dc0b1df8328c274865e70d632c711ba62ec3d3')
        self.assertEqual(key.wif, '5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM')
        self.assertEqual(key.wif_c, 'Kzf6CYbTbBgoQEVXCWLVef1psFkoVjor7mxeyr2TDKWto7iHfXHh')


if __name__ == "__main__":
    unittest.main()
