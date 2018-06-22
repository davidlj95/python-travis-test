"""
Provides methods to encode/decode to/from bech32.

src: https://github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py
"""


# Constants
ALPHABET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l'


def polymod(values):
    generator = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3]
    check = 1

    for value in values:
        top = check >> 25
        check = (check & 0x1ffffff) << 5 ^ value
        for i in range(5):
            check ^= generator[i] if ((top >> i) & 1) else 0

    return check


def hrp_expand(hrp):
    """
    Expand the HRP into values for checksum computation.
    """
    return [ord(x) >> 5 for x in hrp] + [0] + [ord(x) & 31 for x in hrp]


def create_checksum(hrp, data):
    """
    Compute the checksum values given HRP and data.
    """
    values = hrp_expand(hrp) + data
    pm = polymod(values + [0, 0, 0, 0, 0, 0]) ^ 1
    return [(pm >> 5 * (5 - i)) & 31 for i in range(6)]


def verify_checksum(hrp, data):
    return polymod(hrp_expand(hrp) + data) == 1


def convertbits(data, frombits, tobits, padding=True):
    """
    General power-of-2 base conversion.
    """
    acc, bits = 0, 0
    res = []
    maxv = (1 << tobits) - 1
    max_acc = (1 << (frombits + tobits - 1)) - 1

    for value in data:
        if value < 0 or (value >> frombits):
            raise ValueError("")

        acc = ((acc << frombits) | value) & max_acc
        bits += frombits
        while bits >= tobits:
            bits -= tobits
            res.append((acc >> bits) & maxv)

    if padding:
        if bits:
            res.append((acc << (tobits - bits)) & maxv)
    elif bits >= frombits or ((acc << (tobits - bits)) & maxv):
        if ((acc << (tobits - bits)) & maxv):
            print("second case")

        return None

    return res


def encode(hrp, version, program):
    """
    Encodes bytes using bech32 convention into an human-readable string.

    src: https://github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py
    """
    data = [version] + convertbits(program, 8, 5)

    checksum = create_checksum(hrp, data)

    data = data + checksum

    data_coded = ''
    for el in data:
        data_coded += ALPHABET[el]

    return hrp + '1' + data_coded


def decode(string):
    """
    Decodes a bech32 string into a bytes object.
    """
    hr_idx = string.rfind('1')

    # Check position
    if hr_idx < 1 or hr_idx > len(string) - 7 or len(string) > 90:
        # Error
        pass

    hrp = string[:hr_idx]
    data = string[hr_idx+1:]

    # Check charset
    for char in data:
        if char not in ALPHABET:
            raise ValueError("Character not valid to decode from bech32")

    data_decoded = [ALPHABET.find(el) for el in data]

    # Check checksum
    if not verify_checksum(hrp, data_decoded):
        raise ValueError("Checksum not valid")

    # Retrieve version & checksum
    version = data_decoded[0]
    data_decoded = data_decoded[1:-6]

    decoded = convertbits(data_decoded, 5, 8, False)

    return hrp, version, bytes(decoded)
