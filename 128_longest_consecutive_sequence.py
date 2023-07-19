# Problem description: Given an unsorted array of integers nums, return
# The length of the longest consecutive elements sequence. Algorithm must
# run in O(n) time
# My initial thoughts: We can sort the array and then find the sequences that way
# however that would mean O(nlogn) complexity.


# TODO my first implmentation. Naive and doesn't work all the time, works but not for [0, 1, 1, 2] gets 2 but expected 3
# Updated: now fixed but not O(n) complexity
def longest_consecutive(nums):
    # Sort numbers and remove the duplicates as they won't contribute to the count.
    sorted_nums = sorted([*set(nums)])
    longest = 0
    current = 0
    # Iterate through the list
    for i in range(len(sorted_nums)):
        # If we are starting, initialize the longest count to 1
        if i == 0:
            current += 1
            longest = current
        else:
            # If the previous element is consecutive, add 1 to count and then check if we need to update longest
            if sorted_nums[i-1] + 1 == sorted_nums[i]:
                current +=  1
                if longest <= current:
                    longest = current
            # Else not consecutive and reset current to 1
            else:
                current = 1

    return longest

