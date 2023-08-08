# This is a O(n) solution, the idea is to maintain two hashmaps that contain the counts of the characters in the string t
# and the current window. We move the window forward and each time check to see if we matched the number of counts, if matched,
# we update the result and try to shrink the window until it no longer matches.
def minWindow(s: str, t: str) -> str:
    counts = {}
    original_counts = {}
    match = 0
    expected = len(t)
    result = ""
    result_length = float('inf')  # Initialize with positive infinity
    # this is the hash map containing the counts of chars in t
    for i in t:
        original_counts[i] = original_counts.get(i, 0) + 1
    l = 0

    # This is the sliding window
    for i in range(len(s)):
        if s[i] in original_counts:
            counts[s[i]] = counts.get(s[i], 0) + 1
            if counts[s[i]] <= original_counts[s[i]]:
                match += 1
        while match == expected:
            if result_length > i - l + 1:
                result_length = i - l + 1
                result = s[l:i+1]  # Include the end index
            if s[l] in original_counts:
                counts[s[l]] -= 1
                if counts[s[l]] < original_counts[s[l]]:
                    match -= 1
            l += 1

    return result