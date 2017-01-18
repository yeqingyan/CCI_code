""" Question 1.5 """


def one_away(str1, str2):
    """  Check if two strings are one or zero edit away """
    length1 = len(str1)
    length2 = len(str2)
    # replace/same: same length
    if length1 == length2:
        differ_count = 0
        for i in range(0, length1):
            if str1[i] != str2[i]:
                differ_count += 1
        return differ_count < 2
    # insert/remove: length differ by 1
    elif abs(length1 - length2) == 1:
        if length1 > length2:
            short_str, long_str = str2, str1
        else:
            short_str, long_str = str1, str2

        short_length = len(short_str)
        long_length = len(long_str)
        short_index, long_index = 0, 0
        while short_index < short_length and long_index < long_length:
            if long_str[long_index] != short_str[short_index]:
                if long_index != short_index:
                    return False
                else:
                    long_index += 1
            else:
                long_index += 1
                short_index += 1
        return True
    else:
        return False

assert one_away("pale", "ple") is True
assert one_away("pales", "pale") is True
assert one_away("pale", "bale") is True
assert one_away("pale", "bake`") is False