class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                j = i + 1
                k = 1
                while k <len(needle) and haystack[j] == needle[k]:
                    j += 1
                    k += 1
                if k == len(needle):
                    return i
            i += 1