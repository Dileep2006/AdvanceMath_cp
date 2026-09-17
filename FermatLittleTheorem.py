def fermat(a, p):
    return pow(a, p-2, p)

print(fermat(3,7))