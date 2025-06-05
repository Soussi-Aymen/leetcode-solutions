class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num <= first:  
                first = num  # Smallest element so far
            elif num <= second:  
                second = num  # Second smallest element so far
            else:  
                return True  # Found third number greater than `first` and `second`

        return False