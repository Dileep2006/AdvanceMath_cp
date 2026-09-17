## Diophantine equation has a solution if and only if the gcd of a and b divides c.
## Let g = gcd(a, b), then if c % g == 0, a solution exists otherwise no solution exists.

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def Diophantine(a,b,c):
    g = gcd(a,b)

    if c % g == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    Diophantine(a,b,c)