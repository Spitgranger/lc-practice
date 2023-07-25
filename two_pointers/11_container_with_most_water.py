# This solution uses two pointers and a greedy approach to maximize the area, the algorithm runs
# through the input array once, giving time complexity of O(n) and space complexity of O(1)

def max_area(height):
    start = 0
    end = len(height) - 1
    result = 0
    current = 0
    while start < end:
        # Calculate the area of the container
        current = min(height[start], height[end]) * (end - start)
        # Update the max area
        result = max(result, current)
        # Now update pointers, using the logic that the only way to increase the area would be to increase
        # the height that is smaller, if they are equal, move any one
        if height[start] < height[end]:
            start += 1
        elif height[start] > height[end]:
            end -= 1
        else:
            start += 1
    return result
