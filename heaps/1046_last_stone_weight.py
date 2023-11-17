from typing import List
import heapq
def lastStoneWeight(stones: List[int]) -> int:
        #Create a heap in n time, multiply every element by -1 to get a max heap.
        heap = []
        for i in stones:
            heap.append(-1*i)
        heapq.heapify(heap)
        # While there are stills stones left to play the game, play
        while len(heap) > 1:
            # Get the two max elements
            first = -1 * heapq.heappop(heap)
            second = -1 * heapq.heappop(heap)
            # We know first is either greater or equal to second (max heap), so if not equal second is smaller and 
            # the weight of the resulting stone is first - second
            if first != second:
                heapq.heappush(heap, -1 * (first-second))
        # If there are elements left in the heap return that weight, else return 0
        return -1*heap[0] if len(heap) == 1 else 0