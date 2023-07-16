# In this solution, two passes of the nums array is required. One to calculate the prefix product
# of all the positions in the array, and then another starting from the end of the nums array to
# calculate the postfix products of all positions in the array. The prefixes are calculated first
# and stored in the output array, then the postfixes are calculated and multiplied with the element
# in the output (prefix) to get the final result. This requires O(n) time and O(1) space as the output
# does not count in the space complexity analysis.
def product_except_self(nums):
    answer = []
    prefix = 1
    postfix = 1
    for i in range(len(nums)):
        answer.append(prefix)
        prefix *= nums[i]
    for i in range(len(nums), 0, -1):
        answer[i - 1] *= postfix
        postfix *= nums[i - 1]

    return answer


product_except_self([1, 2, 3, 4])
