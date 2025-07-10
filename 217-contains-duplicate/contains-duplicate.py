from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter_nums = Counter(nums)

        for val in counter_nums.values():
            if val > 1:
                return True
        
        return False