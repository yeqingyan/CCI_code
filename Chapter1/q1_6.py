""" Question 1.6  """


def string_compression(string):
    """ Compress string using the counts of repeated characters """
    if not string:
        return string

    compressed_str = ""
    last_char = string[0]
    count = 1
    for char in string[1:]:
        if char == last_char:
            count += 1
        else:
            compressed_str += last_char + str(count)
            last_char = char
            count = 1
    compressed_str += last_char + str(count)
    return compressed_str if len(compressed_str) < len(string) else string

assert string_compression("aabcccccaaa") == "a2b1c5a3"

