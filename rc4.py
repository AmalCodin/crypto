def rc4(key, text):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    i = j = 0
    result = []
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream = S[(S[i] + S[j]) % 256]
        result.append(char ^ keystream)
    
    return bytes(result)

# Example usage
key = b"key"
plaintext = b"HELLO"
ciphertext = rc4(key, plaintext)
decrypted = rc4(key, ciphertext)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted.decode())

