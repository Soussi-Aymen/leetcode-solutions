class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    k = j
                    while k < len(nums2) and nums2[k] <= nums2[j]:
                        k += 1
                    if k == len(nums2):
                        result.append(-1)
                    else:
                        result.append(nums2[k])
            i += 1
        return result 