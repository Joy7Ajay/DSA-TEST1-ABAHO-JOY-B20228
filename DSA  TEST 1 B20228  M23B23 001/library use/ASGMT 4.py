import math
import numpy as np

def test_numbers(arr):
    complex_nums = np.iscomplex(arr)
    real_nums = np.isreal(arr)
    scalar_nums = np.isscalar(arr)

    return complex_nums, real_nums, scalar_nums

# Test array
nums = np.array([1, 2+3j, 4, 5.7, np.nan, np.inf, 1j, 0+0j])

complex_nums, real_nums, scalar_nums = test_numbers(nums)

print("Complex numbers in the array:", nums[complex_nums])
print("Real numbers in the array:", nums[real_nums])
print("Scalar numbers in the array:", nums[scalar_nums])
