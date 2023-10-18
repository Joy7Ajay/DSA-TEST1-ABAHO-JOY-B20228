import math

def smallest_multiple(n):
    factors = [] # List to store the prime factors
    multiple = 1 # Variable to store the smallest multiple

    for i in range(2, n + 1):
        if multiple % i != 0:
            for j in factors:
                if i % j == 0:
                    i //= j
            factors.append(i) # Add the prime factor to the list
            multiple *= i  # Multiply the prime factor to the multiple

    return multiple, factors

n = 13
smallest_multiple, factors = smallest_multiple(n)

# Print the factors of the smallest multiple
print("\nFactors of the smallest multiple:\n", factors)
# Print the smallest multiple of the first n numbers
print("\nSmallest multiple of the first", n, "numbers is:\n", smallest_multiple)

