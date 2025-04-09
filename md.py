import struct
import math

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

# Constants for MD5
s = [7, 12, 17, 22] * 4 + \
    [5, 9, 14, 20] * 4 + \
    [4, 11, 16, 23] * 4 + \
    [6, 10, 15, 21] * 4

K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

# Initial hash values
INIT_A = 0x67452301
INIT_B = 0xEFCDAB89
INIT_C = 0x98BADCFE
INIT_D = 0x10325476

def md5(message):
    message = bytearray(message, 'utf-8')  # Convert to bytes
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff

    # Append the bit '1' to the message
    message.append(0x80)

    # Pad message with zeros until its length is 64 bits less than a multiple of 512
    while (len(message) * 8) % 512 != 448:
        message.append(0)

    # Append original length as a 64-bit little-endian integer
    message += struct.pack('<Q', orig_len_in_bits)

    # Initialize hash values
    A, B, C, D = INIT_A, INIT_B, INIT_C, INIT_D

    for offset in range(0, len(message), 64):
        a, b, c, d = A, B, C, D
        chunk = message[offset:offset + 64]
        M = list(struct.unpack('<16I', chunk))

        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(f, s[i])) & 0xFFFFFFFF

        # Add this chunk's hash to result so far
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Output final digest
    return ''.join(format(x, '02x') for x in struct.pack('<4I', A, B, C, D))

# Test
print(md5("hello"))  # Expected: 5d41402abc4b2a76b9719d911017c592
print(md5("world"))  # Expected: 7d793037a0760186574b0282f2f435e7
