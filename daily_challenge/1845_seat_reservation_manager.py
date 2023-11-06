# Very simple idea. Start with a min heap filled with all available seats. Every call to reserve will pop the min element off heap in constant time
# Every call to unreserve will add that seatNumber back to the heap in log(n) time.
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.size = n
        self.seats = [i + 1 for i in range(n)]

    def reserve(self) -> int: 
        ret = heapq.heappop(self.seats)
        return ret
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)