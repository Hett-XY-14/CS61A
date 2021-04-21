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
