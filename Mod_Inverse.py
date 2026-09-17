def extgcd(a, b):

    if b == 0:
        return a, 1, 0
    gcd, x, y = extgcd(b, a%b)

    x1 = y
    y1 = x - (a//b) * y

    return gcd, x1, y1

def Mod_inverse(a, m):
    gcd, x, y = extgcd(a, m)

    if gcd != 1:
        return -1
    return (x%m+m)%m

print(Mod_inverse(3, 7))