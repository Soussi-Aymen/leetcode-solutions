class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_set = set()
        left = 0
        long_unique_sub = 0
        for right in range(len(s)):
            while s[right] in sub_set:
                sub_set.remove(s[left])
                left += 1
            sub_set.add(s[right])
            long_unique_sub = max(long_unique_sub,right-left+1)

        return long_unique_sub