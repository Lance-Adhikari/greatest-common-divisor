def gcd_naive(a, b):
    best = 0

    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            best = d

    return best

gcd_first = int(input("Enter First Number: "))
gcd_second = int(input("Enter Second Number: "))

print(gcd_naive(gcd_first, gcd_second))