import unittest
from bitcoinaddress import Key, Address, Seed


class TestAddress(unittest.TestCase):

    def testFromWIF(self):
        # given
        key = Key.of('5JbTZ4zCTn1rwCfdkPWLddFgqzieGaG9Qjp3iRhf7R8gNroj4KM')
        address = Address.of(key)

        # then
        self.assertEqual(address.pubkey.upper(),
                         "04E61341F46B529B0FAC2C5E15A67AF7AFFCEB2BE7544AF18D14206FFF041C02C04D6CA36C97F458CFE5754CE15A8F32D4C917B5F0F5E336042EE3BE77C3F58222")
        self.assertEqual(address.pubkeyc.upper(), "02E61341F46B529B0FAC2C5E15A67AF7AFFCEB2BE7544AF18D14206FFF041C02C0")

        self.assertEqual(address.mainnet.pubaddr1, "1NaChZV4JJysct8QYcMKFHnQ2SNFpnBund")
        self.assertEqual(address.mainnet.pubaddr1c, "1D7XaU5PbsPxfZeYBcGGyMEqiVvPhtFMUF")
        self.assertEqual(address.mainnet.pubaddr3, "34QhdWUjZjv3HLyvNYgb4AR7ikAfcdzfCW")
        self.assertEqual(address.mainnet.pubaddrbc1_P2WSH,
                         "bc1q6gmqnd9x8q40gusftcxw84sjmdszcp3hv0ur3k7aufvjwzw5y77sl2kknp")
        self.assertEqual(address.mainnet.pubaddrbc1_P2WPKH, "bc1qaj3zyc83azvukfr5kyltf3guyzca44lhzgq6la")

        self.assertEqual(address.testnet.pubaddr1, "n369zca37LR8Pzc2GBKh5CzitRxxhkHDhK")
        self.assertEqual(address.testnet.pubaddr1c, "msdUsXANQtqDSg89uBEeoGTAaVX6bWK3dW")
        self.assertEqual(address.testnet.pubaddr3, "2MuxuhFQmBCRPV8cU3gJTg7QNw6NqTuUm2A")
        self.assertEqual(address.testnet.pubaddrtb1_P2WSH,
                         "tb1q6gmqnd9x8q40gusftcxw84sjmdszcp3hv0ur3k7aufvjwzw5y77sgzqefw")
        self.assertEqual(address.testnet.pubaddrtb1_P2WPKH, "tb1qaj3zyc83azvukfr5kyltf3guyzca44lhgwmfyw")

    def testFromRandomSeed(self):
        # when
        key = Key.of(Seed())
        address = address = Address.of(key)

        # then
        self.assertEqual(len(address.pubkey), 130)
        self.assertEqual(len(address.pubkeyc), 66)

        self.assertEqual(len(address.mainnet.pubaddr1), 34)
        self.assertEqual(len(address.mainnet.pubaddr1c), 34)
        self.assertEqual(len(address.mainnet.pubaddr3), 34)
        self.assertEqual(len(address.mainnet.pubaddrbc1_P2WSH), 62)
        self.assertEqual(len(address.mainnet.pubaddrbc1_P2WPKH), 42)

        self.assertEqual(len(address.testnet.pubaddr1), 34)
        self.assertEqual(len(address.testnet.pubaddr1c), 34)
        self.assertEqual(len(address.testnet.pubaddr3), 35)
        self.assertEqual(len(address.testnet.pubaddrtb1_P2WSH), 62)
        self.assertEqual(len(address.testnet.pubaddrtb1_P2WPKH), 42)


if __name__ == "__main__":
    unittest.main()
