""" Question 1.1 """


def is_unique(string):
    """ Determine a string has all unique characters """
    for i in range(0, len(string)):
        for j in range(0, i):
            if string[j] == string[i]:
                return False
    return True

assert is_unique("fox") is True
assert is_unique("test") is False
