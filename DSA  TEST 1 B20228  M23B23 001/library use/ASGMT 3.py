import math

def smallest_multiple(n):
    factors = []
    multiple = 1

    for i in range(2, n + 1):
        if multiple % i != 0:
            for j in factors:
                if i % j == 0:
                    i //= j
            factors.append(i)
            multiple *= i

    return multiple, factors

n = 13
smallest_multiple, factors = smallest_multiple(n)

print("\nFactors of the smallest multiple:\n", factors)
print("\nSmallest multiple of the first", n, "numbers is:\n", smallest_multiple)

