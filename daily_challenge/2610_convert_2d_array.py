from typing import List


def findMatrix(self, nums: List[int]) -> List[List[int]]:
    rows = {}
    ret = [[]]
    row = 0
    for i in range(len(nums)):
        for j in range(len(ret)):
            if nums[i] not in ret[j]:
                ret[j].append(nums[i])
                break
            else:
                if j == len(ret) - 1:
                    ret.append([nums[i]])
    return ret
