# Given an interger array nums, return all the triplets [nums[i], nums[i], nums[k]]
# Such that i!=j i!=k j!=k and nums[i]+nums[j]+nums[k] = 0

def threeSum(nums):
    sorted_array = sorted(nums)
    end = len(nums) - 1
    return_array = []
    for i in range(len(nums)):
        if i > 0 and sorted_array[i] == sorted_array[i - 1]:
            print("not")
            continue
        start = i + 1
        while start < end:
            sum = sorted_array[start] + sorted_array[end] + sorted_array[i]
            if sum < 0:
                start += 1
            elif sum > 0:
                end -= 1
            else:
                return_array.append([sorted_array[i], sorted_array[start], sorted_array[end]])
                start += 1
                while sorted_array[start] == sorted_array[start - 1] and start < end:
                    start += 1
    return return_array


print(threeSum([0, 0, 0]))
