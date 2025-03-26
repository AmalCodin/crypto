def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

def rsa_sign(hm, d, n):
    return pow(hm, d, n)

def rsa_verify(signature, e, n):
    return pow(signature, e, n)

# Given values
p, q = 13, 17
n = p * q  # Compute n
phi = (p - 1) * (q - 1)  # Compute Euler's totient
e = 7  # Public exponent

d = mod_inverse(e, phi)  # Private exponent
H_M = 31  # Hash of message

# Signature generation
signature = rsa_sign(H_M, d, n)

# Verification
verified_H_M = rsa_verify(signature, e, n)

print("Public key:", (e, n))
print("Private key:", (d, n))
print("Signature:", signature)
print("Verified H(M):", verified_H_M)
print("Signature valid?", verified_H_M == H_M)
