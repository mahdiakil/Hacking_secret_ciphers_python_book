def gcd(a,b):
    # Return GCD of (a,b) using Euclid's Algorithm
    while a != 0:
        a, b = a % b, a
    return b

def find_mode_inverse(a, m):
    # Returns the mod inverse of a % m, which is x such that (a * x % m = 1)
    if gcd(a,m) != 1:
        return None # no mod inverse if a and m are not relatively prime

    # Calculate using the extended Euclidean algorithm
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 
        v1, v2, v3, u3, u2, u3 = (u1 -q * v1), (u2 -q * v2), (u3 -q * v3), v1, v2, v3
    return u1 % m
