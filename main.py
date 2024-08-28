def power(x, n):
    # Base case: anything to the power of 0 is 1
    if n == 0:
        return 1
    # Recursive case: multiply x by the result of power(x, n-1)
    else:
        return x * power(x, n - 1)

# Example usage:
result = power(3, 4)
print(result)  # Output will be 8
