from typing import List


def minOperations(nums: List[int]) -> int:
    counts = {}
    ops = 0
    for i in nums:
        counts.update({i: counts.get(i, 0)+1})
    for k, v in counts:
        if v - 3 >= 0:
            counts[k] = v - 3
            ops += 1
        elif v - 2 >= 0:
            counts[k] = v - 2
            ops += 1
        else:
            return -1
