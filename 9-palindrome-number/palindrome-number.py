class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        if(x==0):
            return True
        originalDigit = x
        reversedDigit=0
        while (x>0):
            lastDigit = x%10
            reversedDigit= reversedDigit *10 +lastDigit
            x= x//10
                
        return reversedDigit ==originalDigit
            