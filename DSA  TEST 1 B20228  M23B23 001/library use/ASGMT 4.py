import math
import numpy as np

def test_numbers(arr):
    # Check if the numbers in the array are complex
    complex_nums = np.iscomplex(arr)
    # Check if the numbers in the array are real
    real_nums = np.isreal(arr)
    # Check if the numbers in the array are scalar
    scalar_nums = np.isscalar(arr)

    return complex_nums, real_nums, scalar_nums

# Test array
nums = np.array([1, 2+3j, 4, 5.7, np.nan, np.inf, 1j, 0+0j])

# Call the test_numbers function
complex_nums, real_nums, scalar_nums = test_numbers(nums)

# Print the complex numbers in the array
print("Complex numbers in the array:", nums[complex_nums])
# Print the real numbers in the array
print("Real numbers in the array:", nums[real_nums])
# Print the scalar numbers in the array
print("Scalar numbers in the array:", nums[scalar_nums])
