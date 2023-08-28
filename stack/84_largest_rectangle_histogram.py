# Solution uses stack. The idea is to calculate the maximum area that can be made with the current rectangle's height

def largestRectangleArea(heights) -> int:
    stack = []
    max_area = 0
    for i, height in enumerate(heights):
        start = i
        while stack and stack[-1][1] > height:
            prev_index, prev_height = stack.pop()
            max_area = max(max_area, prev_height * (i - prev_index))
            start = prev_index
        stack.append((start, height))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area

print(largestRectangleArea([2,4,5,1,2,5]))