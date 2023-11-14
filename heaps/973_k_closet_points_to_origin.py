from typing import List
#doesnt currently work as hashmap does not allow duplicate keys, so if two points have the same distance only one will be returned and repeated.
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        hmap = {}
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            hmap.setdefault(distance, []).append(point)
            heap.append(-1 * distance) 
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        ret = []
        while len(heap) > 0:
            num = heapq.heappop(heap)
            for element in hmap.get(-1*num):
                ret.append(element)
        return ret