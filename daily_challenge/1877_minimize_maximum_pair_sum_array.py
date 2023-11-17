from typing import List
def minPairSum(nums: List[int]) -> int:
        # The idea is to balance the numbers by balancing the pair sums
        # ie. pairing the largest with the smallest, the second largest with the second smallest etc..
        # This will ensure that the max sum is minimized, keeping the difference between sums to a minimum.
        num1 = 0
        num2 = len(nums) - 1
        # Sort in nlog(n) time
        nums = sorted(nums)
        maxsum = 0
        while num1 < num2:
            maxsum = max(nums[num1] + nums[num2], maxsum)
            num1 += 1
            num2 -= 1
        return maxsum
print(minPairSum([3, 5, 2, 3]))