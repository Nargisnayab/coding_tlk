
# create a numbers
def is_prime(n):
    """
    Returns True if n is a prime number, else False.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(7))  # Output: True
print(is_prime(10)) # Output: False
print(is_prime(100)) # Output: Ture
print(is_prime(1000))



