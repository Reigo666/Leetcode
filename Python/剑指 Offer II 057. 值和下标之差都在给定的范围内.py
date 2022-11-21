class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def getId(x):
            return x//(t+1)
        id_val={}

        for i in range(len(nums)):
            id=getId(nums[i])
            
            if i>k:
                id_rm=getId(nums[i-k-1])
                del id_val[id_rm]
            
            if id in id_val:
                return True
            
            if id-1 in id_val:
                if abs(id_val[id-1]-nums[i])<=t:
                    return True
                
            if id+1 in id_val:
                if abs(id_val[id+1]-nums[i])<=t:
                    return True
            
            id_val[id]=nums[i]
            #print(id_val)
        return False
