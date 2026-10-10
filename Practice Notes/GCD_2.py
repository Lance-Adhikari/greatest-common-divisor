def gcd(a, b):
    while b != 0:
        remainder = a % b
        print(a, "%", b, "=", remainder)

        a = b 
        b = remainder 
    return a

gcd_first = int(input("Enter First Number: "))
gcd_second = int(input("Enter Second Number: "))

print("GCD = ", gcd(gcd_second, gcd_second))