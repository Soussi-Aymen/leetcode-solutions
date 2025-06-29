import random

class RandomizedSet:

    def __init__(self):
        self.randomized_set  = set()

    def insert(self, val: int) -> bool:
        result = False
        if val not in self.randomized_set:
            result = True
            self.randomized_set.add(val)
        return result
    def remove(self, val: int) -> bool:
        result = False
        if val in self.randomized_set:
            result = True
            self.randomized_set.remove(val)
        return result
        

    def getRandom(self) -> int:
        return random.choice(list(self.randomized_set))



# Your Randomized_Set object will be instantiated and called as such:
# obj = Randomized_Set()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()