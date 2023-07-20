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

# New implementation should run in O(n) time uses a set to store all the numbers with no repetition
# Finds the sequences of the numbers based looking at the fact that they have no left neighbours
# For every element in the set, check if it has left neighbour, if not it is start of sequence and 
# attempt to find the longest sequence.
def longestConsecutive(nums):
    sorted_nums = set(nums)
    longest = 0 
    current = 0 
    # Go through the elements in the set
    for number in sorted_nums:
        # If no element to the left, it must be the beginning of the sequence
        if number - 1 not in sorted_nums:
            current += 1
            # Loop through and find the length of that sequence
            while True:
                # As long as there is a right neighbour, increment the current count
                if number + 1 in sorted_nums:
                    current += 1
                    number += 1
                # Else is the end of sequence, update longest and reset current
                else:
                    longest = max(current, longest)
                    current = 0 
                    break
    return longest