class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_square_array = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        pos = len(nums) -1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                sorted_square_array[pos] = nums[left]**2
                left += 1
            else:
                sorted_square_array[pos] = nums[right]**2
                right -= 1
            pos -= 1

        return sorted_square_array