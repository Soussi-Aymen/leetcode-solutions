class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet = []
        nums.sort()

        for i in range (len(nums)-2) :
            if i > 0 and nums[i]  == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1 
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    triplet.append([nums[i], nums [left], nums[right]])
                    while left < right  and nums[left] == nums[left+1]:
                        left += 1
                    while right < right  and nums[right] == nums[right-1]:
                        right -= 1
                    left +=1
                    right -1
                elif nums[i] + nums [left] + nums[right] > 0:
                    right -= 1
                else:
                    left +=1
            
        return triplet