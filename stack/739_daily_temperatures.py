#My solution using a montonic decreasing stack to store the temperatures that are greater than the current. THis is o(n) but insert takes very long so see the below improvement.
def dailyTemperatures(temperatures):
    output = []
    stack = []

    for i in range(len(temperatures) - 1, -1, -1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()
        if not stack:
            output.insert(0,0)
            stack.append(i)
            continue
        output.insert(0, stack[-1] - i)
        stack.append(i)
    return output

#Neetcode solution, O(n) use monotonic decreasing stack from right to left to store.
def dailyTemperatures1(temperatures):
    output = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            output[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return output