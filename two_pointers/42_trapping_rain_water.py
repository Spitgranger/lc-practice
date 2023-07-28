# This is the O(n^2) solution it is too slow, so not all test cases are passing
def trap(height):
    maximum = 0
    for i in range(len(height)):
        maxleft = 0
        maxright = 0
        if i == 0 or i == len(height) - 1:
            continue
        start = i
        end = i
        # Find the max heights on either side of the current element
        while start >= 0:
            if maxleft < height[start]:
                maxleft = height[start]
            start -= 1
        while end < len(height):
            if maxright < height[end]:
                maxright = height[end]
            end += 1
        # The maximum water held at any position is equal to the minimum the greatest elements on either
        # side of the current position subtracted by the height at the current position
        maximum += min(maxleft, maxright) - height[i]
    return maximum

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))

# This is the O(n) solution, notice that the minimum of the two pointers will limit how much water can be stored at
# That specific position memory complexity is O(1)
def trap_save(height):
    maximum = 0
    maxleft = height[0]
    maxright = height[len(height) - 1]
    left = 0
    right = len(height) - 1
    while left < right:
        if maxleft <= maxright:
            left += 1
            # We update maxleft before computing the current water stored. This ensures that current water will never
            # be zero as the new maxleft/maxright will always be >= height[left/right] if updated.
            maxleft = max(maxleft, height[left])
            maximum += maxleft - height[left]
        else:
            right -= 1
            maxright = max(maxright, height[right])
            maximum += maxright - height[right]
    return maximum


print(trap_save([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap_save([4,2,0,3,2,5]))


