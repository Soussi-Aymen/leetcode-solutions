class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {1}
        current = str(n)

        while current not in seen:
            seen.add(current)
            summ = 0

            for digit in current:
                digit = int(digit)
                summ += digit ** 2
            
            if summ == 1:
                return True
            current = str(summ)      
        return False