# This solution is O(n log n) we are creating an array of times then checking if they will collide using a montonic
# decresing stack
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    stack = []
    cars = sorted(zip(position, speed))
    time_cars = list(map(lambda n: float(target - n[0]) / n[1], cars))
    for time in time_cars:
        while stack and time >= stack[-1]:
            stack.pop()
        stack.append(time)
    return len(stack)
