
""" 
Write a function that takes in a function cond and a number n and prints numbers from 1 to n where
calling cond on that number returns True
"""


def is_even(x):
    # Even numbers have remainder 0 when divided by 2.
    return x % 2 == 0


def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    if n == 1:
        if cond(n):
            print(n)
        else:
            return
    elif cond(n):
        keep_ints(cond, n-1)
        print(n)
    else:
        keep_ints(cond, n-1)


keep_ints(is_even, 11)

"""
Write a function similar to keep_ints like before, but now it takes in a number n and returns a function
that has one parameter cond. The returned functiion prints out numbers from 1 to n where calling cond on that
number returns True.
"""


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def keep_ints2(cond):
        if n == 1:
            if cond(n):
                print(n)
            else:
                return
        elif cond(n):
            keep_ints(cond, n-1)
            print(n)
        else:
            keep_ints(cond, n-1)
    return keep_ints2


make_keeper(5)(is_even)

"""
Write a function and_add that takes a one-argument function f and a number n as arguments. It should return a 
function that takes one argument, and does the same thing as the function f, except also adds n to the result
"""


def and_add(f, n):
    """Return a new function. This new function takes an
    argument x and returns f(x) + n.
    >>> def square(x):
    ... return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    def new_f(m):
        return f(m) + n

    return new_f


def square(x):
    return x * x


new_square = and_add(square, 3)
new_square(4)
print(new_square(4))
