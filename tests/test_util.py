import unittest
from bitcoinaddress.util import ripemd


class TestUtil(unittest.TestCase):

    def testRIPEMD(self):
        # given
        hash1 = ripemd("The quick brown fox jumps over the lazy dog".encode())
        hash2 = ripemd("The quick brown fox jumps over the lazy cog".encode())

        # then
        self.assertEqual(hash1.hexdigest(), "37f332f68db77bd9d7edd4969571ad671cf9dd3b")
        self.assertEqual(hash2.hexdigest(), "132072df690933835eb8b6ad0b77e7b6f14acad7")


if __name__ == "__main__":
    unittest.main()
