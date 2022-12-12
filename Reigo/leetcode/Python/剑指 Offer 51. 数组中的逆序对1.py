class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        vec=[]
        for i in range(len(nums)):
            vec.append([nums[i],i])
        vec.sort(key=lambda x:(x[0],x[1]))

        #print(vec)
        sl=[]

        ans=0
        for i in range(len(vec)):
            val,pos=vec[i]
            idx=bisect.bisect(sl,pos)
            ans+=len(sl)-idx
            sl.insert(idx,pos)
        return ans