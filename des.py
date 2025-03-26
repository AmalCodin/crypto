def permute(block, table):
    return [block[i - 1] for i in table]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def feistel_function(right_half, key):
    return xor(right_half, key)  # Simplified function (XOR with key)

def split_half(block):
    mid = len(block) // 2
    return block[:mid], block[mid:]

def des_encrypt(plaintext, key):
    plaintext_bits = [int(b) for b in plaintext]
    key_bits = [int(b) for b in key]
    
    initial_permutation_table = [2, 6, 3, 1, 4, 8, 5, 7]
    plaintext_bits = permute(plaintext_bits, initial_permutation_table)
    
    left, right = split_half(plaintext_bits)
    for _ in range(2):  # Simplified 2-round DES
        temp = right
        right = xor(left, feistel_function(right, key_bits))
        left = temp
    
    final_permutation_table = [4, 1, 3, 5, 7, 2, 8, 6]
    ciphertext_bits = permute(left + right, final_permutation_table)
    
    return "".join(map(str, ciphertext_bits))

# Example usage
plaintext = "10101010"  # 8-bit input
key = "11001100"  # 8-bit key
ciphertext = des_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

