from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = Counter(nums)

        for val in nums.values():
            if val > 1:
                return True
        
        return False