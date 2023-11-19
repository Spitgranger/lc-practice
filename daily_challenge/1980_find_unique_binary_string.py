from typing import List
# Simple dfs to search all possible binary expressions of length len(list[0]), break recursion when one element is found.
def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        def dfs(letter, current):
            if len(current) > len(nums[0]) or len(ans) > 0:
                return
            if current + letter not in nums and len(current + letter) == len(nums[0]) :
                ans.append(current + letter)
            dfs("0",current + letter)
            dfs("1", current + letter)
        dfs("0", "")
        dfs("1", "")
        return ans[0]     