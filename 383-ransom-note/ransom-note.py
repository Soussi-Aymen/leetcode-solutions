from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ransomNote = Counter(ransomNote)
        freq_magazine = Counter(magazine)
        for char, val in freq_ransomNote.items():
            if freq_magazine.get(char,0) < val:
                return False
        return True