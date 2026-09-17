def totient(n):
    res = n

    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            # the main formula res = res * (1 - 1/p) where p is a distinct prime factor
            res -= res // p
        p += 1

    if n > 1:
        res -= res // n
    
    return res

print(totient(10))