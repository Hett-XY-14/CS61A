# R e c u r s i o n
"""Write a fucntion that takes two numbers m and n and returns their product.
Assume m and n are positive integers. Use recursion not mul or *!
"""


def recursive_mul(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1 + recursive_mul(num1, num2-1)


print(recursive_mul(3, 6))

"""In discussion 1, we implemented the function is_prime, which takes in a positive integer and returns whether or not that integer is prime, iteratively.

Now, let's implement it recursively! As a remainder, an integer is considered prime if it has exactly two unique factors: 1 and itself"""


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
        False
    >>> is_prime(1)
        False
    """
    def prime_helper(n, divisor):
        if divisor == 1:
            return True
        elif n == 1 or n % divisor == 0:
            return False
        else:
            return prime_helper(n, divisor-1)
    return prime_helper(n, n-1)


print(is_prime(7))
print(is_prime(10))
print(is_prime(1))
print(is_prime(17))

# T r e e   r e c u r s i o n
"""You want to go up a flight of stairs that has n steps. YOu can either take 1 or 2 steps each time. Hw many different ways can  you go up this flight of stairs. Write a function count_stair_ways that solves this problem. Assume n is positive.
"""


def count_stair_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)


print(count_stair_ways(4))

""" Consider a special version of the count_stairways problem, where instead of taking 1 or 2 steps, we are able to take up to and including k steps at a time.
Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive. """


def count_k(n, k):
    """"
    >>> count_k(3,3)
    4
    >>> count_k(4,4)
        8
    >>> count_k(10,3)
        274
    >>> count_k(300,1)
        1
    """
    ways = 0
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n-i, k)
            i += 1
        return total


print(count_k(10, 3))
