from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        top_k = freq.most_common(k)
        return [ counter[0] for counter in top_k ]        