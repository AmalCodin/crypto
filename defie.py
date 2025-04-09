import random

def generate_private_key(prime):
    return random.randint(2, prime - 2)  # Private key in range [2, p-2]

def calculate_public_key(base, private_key, prime):
    return (base ** private_key) % prime

def calculate_shared_secret(public_key, private_key, prime):
    return (public_key ** private_key) % prime

def diffie_hellman_key_exchange():
    # Publicly known prime number (p) and base (g)
    prime = 23  # Small prime for example only
    base = 5    # Primitive root modulo 23

    # Alice and Bob generate their private keys
    private_key_alice = generate_private_key(prime)
    private_key_bob = generate_private_key(prime)

    # Compute public keys
    public_key_alice = calculate_public_key(base, private_key_alice, prime)
    public_key_bob = calculate_public_key(base, private_key_bob, prime)

    # Compute shared secret
    shared_secret_alice = calculate_shared_secret(public_key_bob, private_key_alice, prime)
    shared_secret_bob = calculate_shared_secret(public_key_alice, private_key_bob, prime)

    # The computed shared secrets should match
    assert shared_secret_alice == shared_secret_bob

    # Output
    print("Prime (p):", prime)
    print("Base (g):", base)
    print("Alice's Private Key:", private_key_alice)
    print("Bob's Private Key:", private_key_bob)
    print("Alice's Public Key:", public_key_alice)
    print("Bob's Public Key:", public_key_bob)
    print("Shared Secret (computed by Alice and Bob):", shared_secret_alice)

diffie_hellman_key_exchange()
