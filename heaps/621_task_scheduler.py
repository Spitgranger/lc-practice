from typing import List
import heapq
from collections import deque
def leastInterval(self, tasks: List[str], n: int) -> int:
        #Use heap and queye to keep track of the next task and when the tasks can be readded to queue respectively
        counts = {}
        for element in tasks:
            counts.update({element: counts.setdefault(element, 0) + 1})
        heap = [-1 * element for element in counts.values()]
        heapq.heapify(heap)
        time = 0
        q = deque()  # this is a pair of (-count, idle time)

        while heap or q:
            time += 1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
                
        return time

