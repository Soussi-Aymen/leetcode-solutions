class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        hash_map = {}
        used_words = set()
        for i in range(len(s)):
            if pattern[i] not in hash_map:
                if s[i] in used_words:
                    return False
                hash_map[pattern[i]] = s[i]
                used_words.add(s[i])
            elif hash_map[pattern[i]] != s[i]:
                return False
        return True
