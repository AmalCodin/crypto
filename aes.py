S_BOX = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5],
    [0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76]
]  # Simplified S-Box

def sub_bytes(state):
    return [[S_BOX[row % 2][col % 8] for col in range(4)] for row in range(4)]

def shift_rows(state):
    return [state[row][row:] + state[row][:row] for row in range(4)]

def add_round_key(state, key):
    return [[state[row][col] ^ key[row][col] for col in range(4)] for row in range(4)]

def aes_encrypt(plaintext, key):
    state = [[ord(c) for c in plaintext[i:i+4]] for i in range(0, 16, 4)]
    round_key = [[ord(c) for c in key[i:i+4]] for i in range(0, 16, 4)]
    state = add_round_key(state, round_key)
    state = sub_bytes(state)
    state = shift_rows(state)
    return state

# Example usage
plaintext = "ABCDEFGHIJKLMNOP"  # 16-byte input
key = "1234567890ABCDEF"  # 16-byte key
ciphertext = aes_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
