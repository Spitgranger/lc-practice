from collections import deque


class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while (True):
            if self.requests[0] < (t - 3000):
                self.requests.popleft()
            else:
                break
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# The solution is to use a queue to maintain the elements that are no longer needed. As values of t are strictly increasing, we can see that for each ping received we
# put it on the queue and then check the front of the queue to see if that element has time less than t - 3000 and if it does remove it and repeat until the head of the
# queue is >= t-3000, then return the length of the requests.
