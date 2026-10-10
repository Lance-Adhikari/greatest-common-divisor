# Greatest Common Divisor

Two Python approaches to finding the greatest common divisor (GCD): a naive divisor search and the Euclidean algorithm.

I built this project while practicing algorithms through Coursera as a first-year Computing Science student at the University of Alberta.

## The problem

For two positive integers, find the largest positive integer that divides both without a remainder. For example, **gcd(18, 24) = 6**.

## Solutions

| File | Approach | Time | Extra space |
| --- | --- | --- | --- |
| [GCD_1.py](GCD_1.py) | Check every possible divisor | O(min(a, b)) | O(1) |
| [GCD_2.py](GCD_2.py) | Euclidean algorithm | O(log(min(a, b))) iterations* | O(1) |

*The case where the smaller positive input is 1 takes constant time. These estimates treat arithmetic operations as constant time and exclude printed output; Python's arbitrary-size integer operations also depend on the number of digits.

### Naive search

`gcd_naive(a, b)` checks every integer from 1 through the smaller input. Whenever a candidate divides both numbers, it updates `best`. Checking in ascending order means the last matching candidate is the greatest common divisor.

For 18 and 24, the common divisors encountered are 1, 2, 3, and 6.

### Euclidean algorithm

`gcd(a, b)` uses the identity `gcd(a, b) = gcd(b, a % b)`. Each iteration prints the remainder calculation and replaces the pair with `(b, remainder)`. When the second value becomes zero, the first value is the GCD.

For 18 and 24:

```text
18 % 24 = 18
24 % 18 = 6
18 % 6 = 0
GCD =  6
```

Taking remainders reduces the problem quickly instead of checking every possible divisor.

## Run locally

Python 3 is required. No extra packages are needed.

```bash
git clone https://github.com/Lance-Adhikari/greatest-common-divisor.git
cd greatest-common-divisor
python GCD_1.py
python GCD_2.py
```

Each script prompts for two integers, one at a time. The first script prints the result; the second prints the remainder steps followed by the result.

## Input assumptions

Use positive integers for comparing these solutions. The naive implementation can return 0 for zero or negative inputs because its search loop is empty. Neither script validates input, and non-integer input raises a `ValueError`.

## Verification

Both scripts were checked against Python's `math.gcd` for these inputs:

| First input | Second input | Expected GCD |
| --- | --- | --- |
| 18 | 24 | 6 |
| 24 | 18 | 6 |
| 17 | 13 | 1 |
| 42 | 42 | 42 |
| 1 | 9 | 1 |
| 28851538 | 1183019 | 17657 |

All six cases passed for both scripts. These are sample checks, not an exhaustive test suite.

## What I learned

- A straightforward search provides a useful starting point for solving a problem.
- The Euclidean algorithm performs far fewer steps for large inputs.
- Testing different inputs helps catch mistakes at the function's call site, as well as in the algorithm itself.

This repository contains my practice code and explanations; course materials and assignment statements are not included.
