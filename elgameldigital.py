def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def modexp(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def simple_hash(message):
    return sum(ord(c) for c in message) % 1000

def generate_keys(p, g, x):
    y = modexp(g, x, p)
    return (p, g, y), x 

# --- Signature Generation ---
def sign(message, p, g, x, k):
    h = simple_hash(message)
    while gcd(k, p - 1) != 1:
        k += 1
    r = modexp(g, k, p)
    k_inv = modinv(k, p - 1)
    s = (k_inv * (h - x * r)) % (p - 1)
    return (r, s)

def verify(message, signature, p, g, y):
    r, s = signature
    if not (0 < r < p):
        return False
    h = simple_hash(message)
    left = (modexp(y, r, p) * modexp(r, s, p)) % p
    right = modexp(g, h, p)
    return left == right

p = 467  
g = 2    
x = 127  
k = 67   

public_key, private_key = generate_keys(p, g, x)
msg = "Hello ElGamal"
signature = sign(msg, p, g, x, k)

print("Message:", msg)
print("Signature:", signature)

valid = verify(msg, signature, p, g, public_key[2])
print("Signature Valid?", valid)
