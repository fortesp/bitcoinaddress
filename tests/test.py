import unittest

from bitcoinaddress.wallet import Wallet

# TODO
class TestBicoinAddress(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_bitcoinaddress(self):
        wallet = Wallet()
        print(wallet)

    def tearDown(self) -> None:
        pass
