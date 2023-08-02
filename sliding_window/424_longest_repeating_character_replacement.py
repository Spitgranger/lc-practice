# import random
# def money():
#     cash = 100000
#     for i in range(100):
#         cash = cash * 0.1*random.randint(-1,1)
#     print(cash)
#
# money()
#
# def money1():
#     cash = 100000
#     for i in range(100000):
#         cash -= 100
#         result = 100
#         for j in range(100):
#             result += result * 0.1*random.randint(-1,1)
#         cash += result
#     print(cash)
# money1()

# This solution is O(26*n) or O(n) time and uses O(n) extra memory. The approach is to use a sliding window
# To keep track if the current substring is valid (meaning length - mostFreqChar <= k) so it means that we can
# replace enough characters to make them all the same. If not valid, we shrink the window. Char counts are kept in
# a hash table, hence the extra memory
def characterReplacement(self, s: str, k: int) -> int:
    start = 0
    longest = 0
    chars = {}
    most_freq = 0
    for i in range(len(s)):
        chars.update({s[i]: chars.get(s[i], 0) + 1})
        for v in chars.values():
            if v > most_freq:
                most_freq = v
        if (i - start + 1) - most_freq <= k:
            longest = max(longest, i - start + 1)
        else:
            chars[s[start]] -= 1
            start += 1
    return longest

# This is a pure O(n) solution. It comes from the realization that there is no need to
# update most_freq when it decreases or stays the same as it has no bearing on the result.
def characterReplacementOptimized(self, s: str, k: int) -> int:
    start = 0
    longest = 0
    chars = {}
    most_freq = 0
    for i in range(len(s)):
        chars.update({s[i]: chars.get(s[i], 0) + 1})
        most_freq = max(most_freq, chars[s[i]])
        if (i - start + 1) - most_freq <= k:
            longest = max(longest, i - start + 1)
        else:
            chars[s[start]] -= 1
            start += 1
    return longest
