def gcd_naive(a, b):
    best = 0

    # Check every possible divisor up to the smaller number.
    for d in range(1, min(a, b) + 1):
        # A common divisor must divide both numbers without a remainder.
        if a % d == 0 and b % d == 0:
            # Divisors increase, so the latest match is the largest so far.
            best = d

    return best


# Read the two integers to compare.
gcd_first = int(input("Enter First Number: "))
gcd_second = int(input("Enter Second Number: "))

print(gcd_naive(gcd_first, gcd_second))
