"""
Tests the methods to encode/decode to/from base58.

src: http://gobittest.appspot.com/Address
"""

# Libraries
import unittest

# Relative imports
from bitcoin import b58encode, b58decode


class TestBase58(unittest.TestCase):
    BYTES = bytes.fromhex("00010966776006953D5567439E5E39F86A0D273BEED61967F6")
    STRING = "16UwLL9Risc3QfPqBUvKofHmBQ7wMtjvM"

    def test_encode(self):
        self.assertEqual(self.STRING, b58encode(self.BYTES))

    def test_decode(self):
        self.assertEqual(self.BYTES, b58decode(self.STRING))
