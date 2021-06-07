# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it

def add_this_many(x, el, lst):
    """Adds 'el' to the end of  lst the number of times x occurs in lst."""
    i = 0
    lst_temp = []
    while i < len(lst):
        if lst[i] == x:
            lst_temp.extend([el])
        i += 1
    lst.extend(lst_temp)


def group_by(s, fn):
    """
    Write a function that takes in a sequence s and a function fn and returns a dictionary.
    The values of the dic itonary are lists of elements from s. Each element e in a list should be
    constructed sch tat fn(e) is the same for all elements in that list. Finally, the key for each
    value should be fn(e)."""

    dict = {}
    for item in s:
        output = fn(item)
        if output in dict.keys():
            dict[output].extend([item])
        else:
            dict[output] = [item]
    return dict


def test_group_by():
    output = group_by([12, 23, 14, 45], lambda p: p//10)
    expected = {1: [12, 14], 2: [23], 4: [45]}
    if output == expected:
        print("Test passed!")
        print("    Results: ")
    else:
        print("Test failed :")
        print("    Results: ")
    print("        expected:    ", expected)
    print("        output:      ", output)


test_group_by()
