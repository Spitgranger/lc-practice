# Problem description: Given an unsorted array of integers nums, return
# The length of the longest consecutive elements sequence. Algorithm must
# run in O(n) time
# My initial thoughts: We can sort the array and then find the sequences that way
# however that would mean O(nlogn) complexity.


# TODO my first implmentation. Naive and doesn't work all the time, works but not for [0, 1, 1, 2] gets 2 but expected 3
def longest_consecutive(nums):
    sorted_nums = sorted(nums)
    longest = 0
    current = 0
    for i in range(len(sorted_nums)):
        if i == 0:
            current += 1
            longest = current
        else:
            if sorted_nums[i-1] + 1 == sorted_nums[i]:
                current += 1
                if longest <= current:
                    longest = current
            else:
                current = 1

    return longest