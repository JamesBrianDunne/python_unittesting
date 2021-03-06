
# x = 'abcaafahbaabdfgz'

# S0ManyAlg0s_


def longest_substring_without_repoeating_chars(string):
    max_length = 0
    for i in range(len(string)):
        max_length = max(max_length, helper(string, i))
    return max_length


def helper(string, start_index):
    seen = set()
    for i in range(start, len(string)):
        if string[i] not in seen:
            seen.add(string[i])
        else:
            return i - start_index

    return len(string) - start_index


print(longest_substring_without_repoeating_chars('abcabcbb') == 3)
print(longest_substring_without_repoeating_chars('bbbbb') == 1)
print(longest_substring_without_repoeating_chars('pwwkew') == 2)
