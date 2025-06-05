class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if i == 0 and len(flowerbed) > 1:
                if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i]= 1
                    n -= 1
            elif i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i]= 1
                n -= 1

            elif i != 0 and i != len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i]= 1
                    n -= 1
 
        return True if n <= 0 else False