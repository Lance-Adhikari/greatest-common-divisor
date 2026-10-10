# Greatest Common Divisor

Two Python approaches to finding the greatest common divisor (GCD): a naive divisor search and the Euclidean algorithm.

## The problem

For two positive integers, find the largest positive integer that divides both without a remainder. For example, **gcd(18, 24) = 6**.

## Solutions

| File | Approach | Time | Extra space |
| --- | --- | --- | --- |
| [GCD_1.py](GCD_1.py) | Check every possible divisor | O(min(a, b)) | O(1) |
| [GCD_2.py](GCD_2.py) | Euclidean algorithm | O(log(min(a, b))) iterations* | O(1) |

### Naive search

`gcd_naive(a, b)` checks every integer from 1 through the smaller input. Whenever a candidate divides both numbers, it updates `best`. Checking in ascending order means the last matching candidate is the greatest common divisor.

For 18 and 24, the common divisors encountered are 1, 2, 3, and 6.

### Euclidean algorithm

`gcd(a, b)` uses the identity `gcd(a, b) = gcd(b, a % b)`. Each iteration prints the remainder calculation and replaces the pair with `(b, remainder)`. When the second value becomes zero, the first value is the GCD.


