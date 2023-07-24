# Given an interger array nums, return all the triplets [nums[i], nums[i], nums[k]]
# Such that i!=j i!=k j!=k and nums[i]+nums[j]+nums[k] = 0

def threeSum(nums):
    # Sort the input array
    sorted_array = sorted(nums)
    return_array = []
    # Fix the first number and use two pointers to find out if the rest of the numbers, excluding repeating neighbours
    for i in range(len(nums)):
        if i > 0 and sorted_array[i] == sorted_array[i - 1]:
            continue
        start = i + 1
        end = len(nums) - 1
        # This is two sum II
        while start < end:
            sum = sorted_array[start] + sorted_array[end] + sorted_array[i]
            if sum < 0:
                start += 1
            elif sum > 0:
                end -= 1
            else:
                # If sum == 0 add the triplet to the return list and keep updating it by one as long as its neighbour
                # is a duplicate, only need to update starting as that enough to prevent duplicate triplets due to
                # code above which will automatically update the ending pointer accordingly.
                return_array.append([sorted_array[i], sorted_array[start], sorted_array[end]])
                start += 1
                while sorted_array[start] == sorted_array[start - 1] and start < end:
                    start += 1
    return return_array


print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
