t = int(input())
while t:
    n = int(input())
    is_prime = True
    if n < 2:
        print("NO")
        continue
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("YES")
    else:
        print("NO")