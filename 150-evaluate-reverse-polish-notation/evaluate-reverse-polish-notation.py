class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(num_1: int, num_2: int, op: str):
            if op == "+":
                return num_1 + num_2
            elif op == "-":
                return num_1 - num_2
            elif op == "*":
                return num_1 * num_2
            else:
                return int(num_1 / num_2)

        stack = []

        for token in tokens:
            if token in ["*", "/", "+", "-"]:
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(operate(num_1, num_2, token))
            else:
                stack.append(int(token))
        
        return stack.pop()