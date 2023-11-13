# Idea is to maintain a min heap with k elements. We know that the largest k elements are in the heap and that the 
# root of the heap will have the kth largest element. 
from typing import List
import heapq
class KthLargest:
    # nlog(n) time, construct heap in n time then potentialy pop n times with each time taking log(n)
    def __init__(self, k: int, nums: List[int]):
        # Construct a heap with all elements of nums
        self.nums = nums
        heapq.heapify(self.nums)
        # pop elements while the size of the heap is greater than k, remaining k elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        self.k = k
        
    # m log(n) complexity
    def add(self, val: int) -> int:            
        # Add to heap
        heapq.heappush(self.nums, val)
        # Pop to maintain the size invariant of K
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # Return the kth largest element
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)