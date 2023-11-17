from typing import List
import math
import heapq
#doesnt currently work as hashmap does not allow duplicate keys, so if two points have the same distance only one will be returned and repeated.
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # Create a min heap in n time
        for point in points:
            distance = point[0]**2 + point[1]**2
            heap.append((distance, point)) 
        heapq.heapify(heap)
        # Then pop k times, which will get the k smallest distances and return those respective points
        ret = []
        for _ in range(k):
             num = heapq.heappop(heap)
             ret.append(num[1])
        return ret
# The total time complexity is n*log(k)