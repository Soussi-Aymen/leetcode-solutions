class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter_s1 = [0] * 26
        counter_s2 = [0] * 26

        for char in s1:
            counter_s1[ord(char) - ord("a")] += 1

        window_size = len(s1)

        for i in range(len(s2)):
            counter_s2[ord(s2[i]) - ord("a")] += 1

            if i >= window_size:
                counter_s2[ord(s2[i-window_size]) - ord("a")] -= 1
            
            if counter_s1 == counter_s2:
                return True
                
        return False