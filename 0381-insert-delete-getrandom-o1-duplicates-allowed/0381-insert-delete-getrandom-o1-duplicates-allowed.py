import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.pos = {}

    def insert(self, val):
       
        not_present = val not in self.pos

    
        self.nums.append(val)

        if val not in self.pos:
            self.pos[val] = set()

        self.pos[val].add(len(self.nums) - 1)

        return not_present

    def remove(self, val):
     
        if val not in self.pos or not self.pos[val]:
            return False

        remove_index = self.pos[val].pop()

        last_value = self.nums[-1]
        last_index = len(self.nums) - 1

        self.nums[remove_index] = last_value

  
        if remove_index != last_index:
            self.pos[last_value].remove(last_index)
            self.pos[last_value].add(remove_index)

        
        self.nums.pop()

    
        if not self.pos[val]:
            del self.pos[val]

        return True

    def getRandom(self):
        return random.choice(self.nums)