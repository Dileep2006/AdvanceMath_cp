def prime_factorization(n):
    factors = []

    p = 2

    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p

        p += 1

    if n > 1:
        factors.append(n)

    return factors

print(prime_factorization(100))