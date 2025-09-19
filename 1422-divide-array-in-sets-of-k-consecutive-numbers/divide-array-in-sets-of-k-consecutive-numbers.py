from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False 
        
        counter = Counter(nums)

        for num in sorted(counter):
            while counter[num] > 0:
                for i in range(k):
                    if counter[num + i] == 0:
                        return False 

                    counter[num + i] -= 1 
        
        return True