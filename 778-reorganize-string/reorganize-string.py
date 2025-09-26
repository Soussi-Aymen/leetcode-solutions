from heapq import heapify, heappush, heappop
from collections import Counter 
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [ (-count, char) for char, count in counter.items()]
        heapify(heap)
        result = []

        while len(heap) > 1:
            count_1, char_1 = heappop(heap)
            count_2, char_2 = heappop(heap)
            result.append(char_1)
            result.append(char_2)
            count_1 += 1
            count_2 += 1

            if count_1  < 0:
                heappush(heap, (count_1, char_1))
            if count_2  < 0:
                heappush(heap, (count_2, char_2))
        if heap:
            count, char = heappop(heap)
            if -count > 1:
                return ""
                
            result.append(char)

        return "".join(result)