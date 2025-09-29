class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0 

        while a > 0 or b > 0 or c > 0:
            a_bit = a % 2
            b_bit = b % 2
            c_bit = c % 2
            
            if (a_bit | b_bit) != c_bit:
                if c_bit == 1:
                    flips += 1
                else:
                    flips += a_bit + b_bit
            
            a //= 2
            b //= 2
            c //= 2
        return flips