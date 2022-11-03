class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        x=0
        for num in nums:
            x=x^num
        n=len(nums)+2
        for i in range(1,n+1):
            x=x^i
        #x=x1^x2
        #print(x)
        lbt=x&(-x)
        #print(lbt)
        type1=0
        type2=0
        for num in nums:
            if lbt&num:
                #print(lbt,num)
                type1^=num
            else:
                type2^=num
        #print(type1,type2)

        for i in range(1,n+1):
            if lbt&i:
                type1^=i
            else:
                type2^=i
        return [type1,type2]
            

