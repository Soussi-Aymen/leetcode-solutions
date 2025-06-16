class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_bracket = {"]": "[", ")": "(", "}": "{"}
        
        for char in s:
            if char in hash_bracket:
                if not stack or stack[-1] != hash_bracket[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
                
        return not stack