from heapq import heappop, heappush

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            ecudiean_distance = sqrt((x**2) + (y**2))
            heappush(heap, (-ecudiean_distance,x,y))
            if len(heap) > k:
                heappop(heap)

        return [[x,y] for _, x, y in heap]