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