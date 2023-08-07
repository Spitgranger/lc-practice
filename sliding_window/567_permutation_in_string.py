# My solution is O(26*n) the idea is to use two hash tables. Each one stores the counts of every character
# in both strings. The first never changes while the second contains the counts of the characters in the current window
# The algorithm goes, start at the first character in s2, increment its count in the hashmap and then compare the counts of characters
# if the counts of the characters is equal to the counts in the hashmap storing s1, a permutation exists.
# If the window becomes greater than the length of s1, move the window forward by removing the last character of the window. Going through,
# if we finish all windows, return false.
def checkInclusion(s1: str, s2: str) -> bool:
    counts = {}
    original_counts = {}
    l = 0
    for i in s1:
        original_counts.update({i: original_counts.get(i, 0) + 1})
    print(original_counts)
    for i in range(len(s2)):
        counts.update({s2[i]: counts.get(s2[i], 0) + 1})
        if i - l + 1 > len(s1):
            counts[s2[l]] -= 1
            l += 1
        count = 0
        flag = False
        for i in original_counts.keys():
            count += 1
            if original_counts.get(i) != counts.get(i):
                flag = True
                break
        if not flag:
            return True
    return False

