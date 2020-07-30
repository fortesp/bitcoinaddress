import unittest

from bitcoinaddress import Address, Key, Wallet


# TODO
class TestBicoinAddress(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_bitcoinaddress(self):

        key = Key()
        keys_dict = key.generate()
        print(keys_dict)

        address = Address(key)
        address_dict = address.generate()
        print(address_dict)

    def tearDown(self) -> None:
        pass
