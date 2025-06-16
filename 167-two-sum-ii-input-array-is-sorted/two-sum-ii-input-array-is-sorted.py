class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        while nums[left] +nums[right] != target:
            if nums[left] +nums[right] < target:
                left += 1
            else:
                right -= 1
        return [left+1, right+1]