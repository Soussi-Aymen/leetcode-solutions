from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heappush(heap, -num)
 
        for i in range(k-1):
            heappop(heap)
        
        return - heappop(heap)