# Greatest Common Divisor

The greatest common divisor (GCD) of two positive integers is the largest positive integer that divides both without a remainder. For example, the GCD of 18 and 24 is 6.

This exercise compares checking every possible divisor with repeatedly taking remainders.

## 1. Naive search — `GCD_1.py`

The `gcd_naive(a, b)` function checks every integer from 1 through the smaller input. Whenever a candidate divides both numbers, it updates `best`. Because candidates are checked in ascending order, the final value is the largest common divisor.

For 18 and 24, the common divisors encountered are 1, 2, 3, and 6, so the result is 6.

- Time: O(min(a, b)) divisor checks.
- Extra space: O(1).
- Intended input: two positive integers. Zero and negative inputs are outside this implementation's intended range; the loop can be empty and return 0.

## 2. Euclidean algorithm — `GCD_2.py`

The `gcd(a, b)` function uses the identity `gcd(a, b) = gcd(b, a % b)`. Each iteration prints the remainder calculation, replaces the pair with `(b, remainder)`, and stops when the second value becomes zero. The first value is then the GCD.

For a function call `gcd(18, 24)`, the steps would be:

```text
18 % 24 = 18
24 % 18 = 6
18 % 6 = 0
```

The result would be 6.

- Time: O(log(min(a, b))) iterations for positive inputs, with a constant-time case when the smaller input is 1.
- Extra space: O(1), excluding printed output.

These complexity descriptions use the usual model where arithmetic operations take constant time; Python's arbitrary-size integer arithmetic also depends on the number of digits.

### Known issue in the current script

The original code is preserved. Its final line currently calls:

```python
gcd(gcd_second, gcd_second)
```

This passes the second input twice and does not use the first input. As a result, running the script with 18 and 24 currently prints:

```text
24 % 24 = 0
GCD =  24
```

The intended call for a future correction is `gcd(gcd_first, gcd_second)`. That correction has **not** been applied to the source file.

## Run locally

From the repository root:

```bash
python "Practice Notes/GCD_1.py"
python "Practice Notes/GCD_2.py"
```

Both scripts prompt for two integers. Non-integer input raises a `ValueError`; input validation is not implemented.

## Verification

The scripts were run with inputs 18 and 24. The naive script returned 6. The Euclidean script returned 24, confirming the call-site issue described above. This is a sample check, not an exhaustive test suite.

## Takeaway

Trying every possible divisor is straightforward but requires more work as the inputs grow. The Euclidean algorithm reduces the problem with each remainder calculation. This exercise also shows why checking the function's call site matters, even when its core algorithm is correct.
