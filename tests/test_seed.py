import unittest
from bitcoinaddress.key.seed import Seed


class TestSeed(unittest.TestCase):

    def testSeedFixedEntropy(self):
        seed_1 = Seed.of('myseed')
        seed_2 = Seed.of('myseed')

        self.assertIsNotNone(seed_1.__str__())
        self.assertIsNotNone(seed_2.__str__())
        self.assertEqual(seed_1.__str__(), seed_2.__str__())

    def testSeedRandomEntropy(self):
        seed_1 = Seed()
        seed_2 = Seed()

        self.assertIsNotNone(seed_1.__str__())
        self.assertIsNotNone(seed_2.__str__())
        self.assertNotEqual(seed_1.__str__(), seed_2.__str__())


if __name__ == "__main__":
    unittest.main()
