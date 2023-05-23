class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        v_l=list(zip(values,labels))
        v_l.sort(key=lambda x:(-x[0],x[1]))
        cnt=Counter()

        j=0
        ans=0

        for v,l in v_l:
            if cnt[l]<useLimit:
                ans+=v
                cnt[l]+=1
                numWanted-=1
                if numWanted==0:
                    break
        return ans
        # for i in range(numWanted):
        #     while j<len(v_l) and cnt[v_l[j][1]]>=useLimit:
        #         j+=1
        #     if j>=len(v_l):
        #         break
        #     val,idx=v_l[j] 
        #     cnt[idx]+=1
        #     ans+=val
        #     #print(val)
        #     j+=1
        
        return ans
            