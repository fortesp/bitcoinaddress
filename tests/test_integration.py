from unittest import TestCase
from bitcoinaddress import Key, Address
from bitcoinaddress.key import Seed


class TestIntegration(TestCase):

    def testIntegrationKeySeed(self):
        # when
        key1 = Key()
        keys_dict_1 = key1.generate()

        key2 = Key('myseed')
        keys_dict_2 = key2.generate()

        key3 = Key('myseed')
        keys_dict_3 = key3.generate()

        key4 = Key('myseed2')
        keys_dict_4 = key4.generate()

        # then
        self.assertIn('hex', keys_dict_1)
        self.assertEqual(len(keys_dict_1['hex']), 64)
        self.assertIn('wif', keys_dict_1)
        self.assertEqual(len(keys_dict_1['wif']), 51)
        self.assertIn('wifc', keys_dict_1)
        self.assertEqual(len(keys_dict_1['wifc']), 52)
        self.assertIn('testnet', keys_dict_1)

        self.assertTrue(keys_dict_1 != keys_dict_2)
        self.assertFalse(keys_dict_2 != keys_dict_3)
        self.assertTrue(keys_dict_3 != keys_dict_4)

    def testAddress(self):
        # when
        address = Address(Key())
        address_dict = address.generate()

        # then
        self.assertIn('pubkey', address_dict)
        self.assertEqual(len(address_dict['pubkey']), 130)
        self.assertIn('pubkeyc', address_dict)
        self.assertEqual(len(address_dict['pubkeyc']), 66)
        self.assertIn('pubaddr1', address_dict)
        self.assertEqual(len(address_dict['pubaddr1']), 34)
        self.assertIn('pubaddr3', address_dict)
        self.assertEqual(len(address_dict['pubaddr3']), 34)
        self.assertIn('pubaddrbc1_p2wsh', address_dict)
        self.assertEqual(len(address_dict['pubaddrbc1_p2wsh']), 62)
        self.assertIn('pubaddrbc1_p2wpkh', address_dict)
        self.assertEqual(len(address_dict['pubaddrbc1_p2wpkh']), 42)
        self.assertIn('testnet', address_dict)

    def testKeyAddress(self):
        # when
        key_1 = Key('myseed')
        key_2 = Key('myseed')

        address_1 = Address(key_1)
        address_2 = Address(key_2)

        # then
        self.assertEqual(address_1.pubkey, address_2.pubkey)

    def testKeyAddressSeed(self):
        # when
        seed_1 = Seed('myseed')
        seed_2 = Seed('myseed')
        key_1 = Key(seed_1)
        key_2 = Key(seed_2)

        address_1 = Address(key_1)
        address_2 = Address(key_2)

        # then
        self.assertEqual(address_1.pubkey, address_2.pubkey)
