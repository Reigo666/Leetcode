class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if candidates*2>=len(costs):
            costs.sort()
            return sum(costs[:k])
        else:
            l1=costs[:candidates]
            l2=costs[-candidates:]
            l=candidates
            r=len(costs)-candidates-1
            l1.sort()
            l2.sort()
            ans=0
            cnt=k
            while l<=r and cnt:
                if l1[0]<=l2[0]:
                    #print(l1[0])
                    ans+=l1[0]
                    del l1[0]
                    bisect.insort(l1,costs[l])
                    l+=1
                else:
                    #print(l2[0])
                    ans+=l2[0]
                    del l2[0]
                    bisect.insort(l2,costs[r])
                    r-=1
                cnt-=1
            
            if cnt==0:
                return ans
            l1=l1+l2
            l1.sort()
            #print(l1)
            ans+=sum(l1[:cnt])
            return ans
            
