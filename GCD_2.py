def gcd(a, b):
    # Repeat until the second number becomes zero.
    while b != 0:
        remainder = a % b
        # Display each step of the Euclidean algorithm.
        print(a, "%", b, "=", remainder)

        # Replacing (a, b) with (b, remainder) preserves their GCD.
        a = b
        b = remainder

    # The last nonzero value is the GCD for positive inputs.
    return a


# Read the two integers to compare.
gcd_first = int(input("Enter First Number: "))
gcd_second = int(input("Enter Second Number: "))

print("GCD = ", gcd(gcd_first, gcd_second))
