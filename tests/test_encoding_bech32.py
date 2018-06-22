"""
Tests the methods to encode/decode to/from bech32.

src: http://gobittest.appspot.com/Address
"""

# Libraries
import unittest

# Relative imports
from bitcoin import bech32encode, bech32decode


class TestBech32(unittest.TestCase):
    PROGRAM = bytes.fromhex("751e76e8199196d454941c45d1b3a323f1433bd6")
    HRP = "bc"
    STRING = "bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4"
    VERSION = 0

    PROGRAM2 = bytes.fromhex(
        "1863143c14c5166804bd19203356da136c985678cd4d27a1b8c6329604903262")
    STRING2 = "bc1qrp33g0q5c5txsp9arysrx4k6zdkfs4nce4xj0gdcccefvpysxf3qccfmv3"
    VERSION2 = 0

    def test_encode_p2wpkh(self):
        self.assertEqual(self.STRING, bech32encode(self.HRP,
                                                   self.VERSION, self.PROGRAM))

    def test_decode_p2wpkh(self):
        self.assertEqual((self.HRP, self.VERSION, self.PROGRAM), bech32decode(
            self.STRING))

    def test_encode_p2wsh(self):
        self.assertEqual(self.STRING2, bech32encode(self.HRP, self.VERSION2,
                                                    self.PROGRAM2))

    def test_decode_p2wsh(self):
        self.assertEqual((self.HRP, self.VERSION2, self.PROGRAM2),
                         bech32decode(self.STRING2))
