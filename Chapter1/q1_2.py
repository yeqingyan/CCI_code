""" Question 1.2 """


def check_permutation(str1, str2):
    """ Find if one string is a permutation of the other one """
    string_hash = {}
    for char in str1:
        if char not in string_hash:
            string_hash[char] = 1
        else:
            string_hash[char] += 1

    for char in str2:
        if char not in string_hash or string_hash[char] == 0:
            return False
        else:
            string_hash[char] -= 1
    return True

assert check_permutation("abc", "cba") is True
assert check_permutation("abc", "ccc") is False
