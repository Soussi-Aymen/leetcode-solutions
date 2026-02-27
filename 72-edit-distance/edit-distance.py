class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Only keep current and previous row
        prev = list(range(n + 1))
        
        for i in range(1, m + 1):
            curr = [i]  # First element is number of deletions
            
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr.append(prev[j-1])
                else:
                    curr.append(min(
                        curr[j-1] + 1,   # Insert
                        prev[j] + 1,     # Delete
                        prev[j-1] + 1    # Replace
                    ))
            
            prev = curr
        
        return prev[n]