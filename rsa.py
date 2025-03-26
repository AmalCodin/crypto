def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa_encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(ciphertext, d, n):
    return "".join(chr(pow(char, d, n)) for char in ciphertext)

# Example usage
p, q = 61, 53  # Two prime numbers
n = p * q  # Compute n
phi = (p - 1) * (q - 1)  # Compute Euler's totient

e = 17  # Choose e such that 1 < e < phi and gcd(e, phi) = 1
while gcd(e, phi) != 1:
    e += 1

d = mod_inverse(e, phi)  # Compute private key

message = "HELLO"
ciphertext = rsa_encrypt(message, e, n)
decrypted_message = rsa_decrypt(ciphertext, d, n)

print("Ciphertext:", ciphertext)
print("Decrypted message:", decrypted_message)

