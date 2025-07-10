from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        result = 0
        for jewel in jewels:
            result += stones[jewel]
        
        return result