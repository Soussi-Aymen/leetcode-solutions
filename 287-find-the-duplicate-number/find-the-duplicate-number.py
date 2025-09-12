from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for element, count in freq.items():
            if count > 1: 
                return element
        
        return -1