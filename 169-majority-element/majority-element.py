from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_elements = Counter(nums)
        for key, val in freq_elements.items():
            if val > (len(nums)//2):
                return key