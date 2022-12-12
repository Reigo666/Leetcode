class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        a=list(zip(nums,cost))
        #a.sort()
        minnum=min(nums)
        maxnum=max(nums)
        if minnum==maxnum:
            return 0
        
        l=minnum
        r=maxnum
        
        def calculateCost(a,target):
            temp=0
            for i in range(len(a)):
                temp+=abs(target-a[i][0])*a[i][1]
            return temp
        #lcost=calculateCost(a,minnum)
        #rcost=calculateCost(a,maxnum)
        
        
        midcost=0
        cnt=20
        
        #print(l,r)
        while(l<r):
            #print(l,r)
            #cnt-=1
            #if not cnt:
                #break
            if r-l==1:
                return min(calculateCost(a,l),calculateCost(a,r))
            mid=(l+r)//2
            midl=mid-1
            midr=mid+1
            midcost=calculateCost(a,mid)
            
            midlcost=calculateCost(a,midl)
            
            midrcost=calculateCost(a,midr)
            if midcost<=midlcost and midcost<=midrcost:
                #print(l,r,midlcost,midcost,midrcost)
                return midcost
            elif midlcost<=midcost and midcost<=midrcost:
                r=mid
            else:
                l=mid
            
            #print(l,r,midlcost,midcost,midrcost)
        return midcost

        
        