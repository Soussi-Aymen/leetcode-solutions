from heapq import heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            x = - heappop(heap)
            y = - heappop(heap)
            if (x > y) or (y > x):
                heappush(heap, -abs(x - y))

        return - heap[0] if heap else 0