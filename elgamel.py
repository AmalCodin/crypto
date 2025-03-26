def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def elgamal_encrypt(message, p, g, y, k):
    a = mod_exp(g, k, p)
    b = (mod_exp(y, k, p) * message) % p
    return a, b

def elgamal_decrypt(a, b, x, p):
    s = mod_exp(a, x, p)
    s_inv = pow(s, -1, p)
    return (b * s_inv) % p

# Example usage
p = 23  # Prime number
g = 5   # Primitive root of p
x = 6   # Private key

y = mod_exp(g, x, p)  # Public key component

message = 15  # Plaintext message (must be less than p)
k = 3  # Random integer

a, b = elgamal_encrypt(message, p, g, y, k)
decrypted_message = elgamal_decrypt(a, b, x, p)

print("Ciphertext:", (a, b))
print("Decrypted message:", decrypted_message)

