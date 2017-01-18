""" Question 1.3 """


def urlify(char_array, length):
    """  Replace all spaces in a char array with %20 """
    spaces = 0
    index = 0
    while index < length:
        if char_array[index] == ord(' '):
            spaces += 1
        index += 1
    new_length = length + 2 * spaces

    new_index = new_length - 1
    old_index = length - 1

    while old_index >= 0:
        char = char_array[old_index]
        if char == ord(' '):
            char_array[new_index] = ord('0')
            char_array[new_index-1] = ord('2')
            char_array[new_index-2] = ord('%')
            new_index -= 3
        else:
            char_array[new_index] = char
            new_index -= 1
        old_index -= 1

    return char_array

assert bytes(urlify(bytearray(b"Mr John Smith    "), 13)) == b"Mr%20John%20Smith"

