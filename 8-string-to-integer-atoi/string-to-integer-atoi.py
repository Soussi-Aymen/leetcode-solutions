class Solution:
    def myAtoi(self, s: str) -> int:
        def round_32bit(num: int) -> int:
            INT_MIN= -2**31
            INT_MAX= 2**31 -1
            
            num=  - int(num) if sign == "-" else int(num)
            
            if num < INT_MIN:
                return INT_MIN
            elif num > INT_MAX:
                return INT_MAX
            else:
                return num
        
        s = s.lstrip()
        
        if not s:
            return 0
        
        num = 0
        sign = 1
        i = 0

        if s[i] in ["-", "+"] :
            if s[i] == "-":
                sign = -1
                
            i += 1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i+= 1

        num *= sign
        
        return round_32bit(num)
