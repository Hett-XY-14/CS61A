# Consider an insect in an M by N grid. The insect at the bottom left corner, (0, 0), and wants to end up at the top right corner (M-1, N-1). The insect is onl capable of moving right or up. Write a function paths that takes a grid length and width and returns the number of different paths the insect can take from the start to the goal. (There is a closed-form solution to this problen but try to answer it procedurally using recursion) #

def paths(m, n):
    if (m == 1 or n == 1):
        return 1
    else:
        return paths(m-1, n) + paths(m, n-1)


print(paths(4, 4))

# Write a procedure merge(s1, s2) wich takes two sorted (smallest value first) lists and returns a single list with all of the elements of the two lists, in ascending order. Use recursion.


def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3],[2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if len(s1) == 0:
        return s2
    if len(s2) == 0:
        return s1
    if s1[0] < s2[0]:
        return [s1.pop(0)] + merge(s1, s2)
    else:
        return [s2.pop(0)] + merge(s1, s2)


list1 = [2, 3, 5, 6, 9]
list2 = [1, 4, 7, 8, 10]

print(merge(list1, list2))

# Mario needs to jump over a sequence of Piranha plants, represented as a string of spaces (no plant) and P's (plant!). He only moves forward, and he can either step (move forward one space) or jump (move forward two spaces) from each position. How many different ways can Mario traverse a level without stepping or jumping into a Piranha plant? Assume that every level begins with a space (where Mario starts) and ends with a space (where Mario must end up):


def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps or jumps to reach the end of the level without ever landing in Piranha plant. Assume that every level begins and ends whit a space.

    >>> mario_number(' P P ') # jump , jump
    1
    >>> mario_number(' P P  ') # jump, jum, step
    1
    >>> mario_number('  P P ') # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ') # Mario cannot jump two plants
    0
    >>> mario_number('    ') # step, jump; jump, step; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    total = 0
    if level[0] == 'P':
        return 0
    if len(level) == 1 and level[0] == ' ':
        return 1
    if len(level) > 2:
        return mario_number(level[1:]) + mario_number(level[2:])
    else:
        return mario_number(level[1:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# H  i  g  h  e  r    O  r  d  e  r    F  u  n  c  t  i  o  n  s

""" Express the following lambda expression using a def statement,
and the def statement using a lambda expressión."""


def pow(x, y): return x ** y


def foo(x):
    def f(y):
        def g(z):
            return x + y * z
        return g
    return f


def pow(x, y):
    return x ** y


def foo(x): return lambda y: lambda z: x + y * z
