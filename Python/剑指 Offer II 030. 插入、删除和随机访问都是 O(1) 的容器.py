class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums=[]
        self.num_indices={}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        num_indices=self.num_indices
        nums=self.nums
        
        if val in num_indices:
            return False
        
        num_indices[val]=len(nums)
        nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        num_indices=self.num_indices
        nums=self.nums

        if val not in num_indices:
            return False

        idx=num_indices[val]
        nums[idx]=nums[-1]
        num_indices[nums[-1]]=idx

        nums.pop()
        del num_indices[val]
        return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()