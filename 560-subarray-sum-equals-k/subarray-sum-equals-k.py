from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1   # base case: prefix sum 0 appears once

        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - k]   # how many times needed sum occurred
            freq[prefix_sum] += 1

        return count