# This method used for below 10 pow 6
def totientSieve(n):

    phi = list(range(n + 1))

    for p in range(2, n + 1):
        if phi[p] == p:
            for i in range(p, n + 1, p):
                phi[i] -= phi[i] // p
    
    return phi

n = 10
phi = totientSieve(n)

for i in range(1, n + 1):
    print(f"{i} -> {phi[i]}")