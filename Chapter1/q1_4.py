""" Question 1.4 """


def palindrome_permutation(string):
    """ check if a string is a permutation of a palindrome """
    char_hash = {}

    # Count letters
    for c in string:
        char = c.lower()
        if ord(char) < ord('A') or ord(char) > ord('z'):
            continue 
        if char not in char_hash:
            char_hash[char] = 1
        else:
            char_hash[char] += 1

    odd_letters_count = 0
    for count in char_hash.values():
        if count % 2 != 0:
            odd_letters_count += 1

        if odd_letters_count > 1:
            return False
    return True

assert palindrome_permutation("Tact Coa") is True
assert palindrome_permutation("abbccdaa") is False
