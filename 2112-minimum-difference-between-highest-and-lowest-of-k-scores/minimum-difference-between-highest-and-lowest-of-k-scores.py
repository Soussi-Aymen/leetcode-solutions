class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()
        min_k_difference = float("inf")
        
        for i in range(len(nums)- k + 1):
            min_k_difference = min(min_k_difference, nums[i + k - 1] - nums[i])
        
        return min_k_difference