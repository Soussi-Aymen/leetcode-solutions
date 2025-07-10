from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        map_stones = Counter(stones)
        result = 0
        for jewel in jewels:
            result += map_stones[jewel]
        
        return result