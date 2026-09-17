def Sieve(n):
    
    prime = [True] * (n+1) 
    prime[0] = prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(i*i, n+1, p):
                prime[i] = False
        p += 1
    return [i for i in range(n+1) if prime[i]]


res = Sieve(35)
for num in res:
    print(num, end=" ")
