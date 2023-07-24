# The approach is to use two pointers in this situation as the array is sorted.
# One starting at the front of array, other at end, while these pointers are not 
# crossed check if the sum of the values pointed to by these pointers is greater or
# less than the target value, if greater, decrease the pointer at end, if less, increase
# the pointer at beginning, if equal, return the indexes of the pointers + 1
# This time complexity is O(n)
def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1
    while start <= end:
        sum = numbers[start] + numbers[end]
        if sum < target:
            start += 1
        elif sum > target:
            end -= 1
        elif sum == target:
            return [start+1, end+1]
        
print(twoSum([2,7,11,15], 9))
