"""
Provides methods to encode/decode to/from base58.
"""

# Libraries
import math

# Constants
ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def encode(byte_array):
    """
    Encodes bytes using base58 convention into an human-readable string

    src: https://es.bitcoin.it/wiki/Codificaci%C3%B3n_Base58Check
    """
    assert isinstance(byte_array, bytes), "Expected bytes, given: " + \
                                          type(byte_array)
    output = ""
    # Convert bytes to integer
    number = int.from_bytes(byte_array, byteorder='big')

    while number > 0:
        number, residuum = divmod(number, 58)
        output += ALPHABET[residuum]

    # Convert leading zeros
    leading_zeros = 0

    for element in byte_array:
        if element == 0:
            leading_zeros += 1
        else:
            break

    output += ALPHABET[0] * leading_zeros

    return output[::-1]


def decode(string):
    """
    Decodes a base58 string into a bytes object
    """
    assert isinstance(string, str), "Expected a string object, given: " + \
                                    type(string)
    number = 0

    for char in string:
        number *= 58
        if char not in ALPHABET:
            raise ValueError("Character not valid to decode from Base58")
        number += ALPHABET.index(char)

    # Convert integer to bytes
    number_bytes = number.to_bytes(math.ceil(number.bit_length()/8), "big")

    # Check leading zeros to put them back again
    leading_zeros = 0

    for char in string:
        if char == ALPHABET[0]:
            leading_zeros += 1
        else:
            break
    number_bytes = b'\x00'*leading_zeros + number_bytes

    return number_bytes
