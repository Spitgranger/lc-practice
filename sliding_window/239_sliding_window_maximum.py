import collections
# This is O(n) solution that utilized monotonic queue to find the maximum in each window.
def maxSlidingWindow(nums, k):
    result = []
    deck = collections.deque() #collection of indexes
    l = 0
    r = 0
    while r < len(nums):
        while deck and nums[deck[-1]] < nums[r]:
            deck.pop()
        deck.append(r)
        # remove left value from window when out of bouds
        if l > deck[0]:
            deck.popleft()
        if (r + 1) >= k:
            result.append(nums[deck[0]])
            l += 1
        r += 1
    return result
