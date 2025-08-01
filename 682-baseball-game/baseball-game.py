class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for operation in operations:
            if operation == "+":
                stack.append(stack[-1] + stack[-2])
            elif operation == "D":
                stack.append(stack[-1]*2)
            elif operation == "C":
                if stack:
                    stack.pop()
            else:
                stack.append(int(operation))
        
        return sum(stack)