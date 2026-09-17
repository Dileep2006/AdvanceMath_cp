t = int(input())
arr = [int(input()) for _ in range(t)]

m = max(arr)

spf = [0] * (m + 1)

for p in range(2, int(m ** 0.5) + 1):
    if spf[p] == 0:
        for i in range(p * p, m + 1, p):
            if spf[i] == 0:
                spf[i] = p

for n in arr:
    print(spf[n] if spf[n] else n)