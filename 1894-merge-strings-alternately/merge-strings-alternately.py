class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            result.append(word1[i])
            result.append(word2[i])

        result.append(word1[min_length:] or word2[min_length:])
        
        return "".join(result)