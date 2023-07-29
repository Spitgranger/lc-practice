# This is a O(n) solution. The idea is to maintain a sliding window of the current substring
# with no repeats. We start at position 0 and iterate through the string. If the current element
# is not already in the string, we can update longest with the length of the current substring,
# else, we shrink the window by advancing the starting pointer.
def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    longest = 0
    letter_dict = set()
    # Iterate through string
    for i in range(len(s)):
        # If the current element is in the substring, remove it from the set and shrink the window
        while s[i] in letter_dict:
            letter_dict.remove(s[start])
            start += 1
        # else add the current element to set of chars in substring and recompute the longest substring length
        letter_dict.add(s[i])
        longest = max(i - start + 1, longest)
    return longest

print(lengthOfLongestSubstring("bvbf"))
print(lengthOfLongestSubstring("abcabcbb"))