class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        #newtime=ceil(vat[j]/(bucket[j]+i))+i
        mx=max(vat)
        if mx==0:
            return 0
        
        n=len(bucket)
        #蓄i次水
        #桶的大小需要为 ceil(vat/i)
        ans=inf
        for i in range(1,mx+2):
            need_upgrade=0
            for j in range(n):
                need_bucket=ceil(vat[j]/i)
                # need_upgrade+=max(0,need_bucket-bucket[j])
                if bucket[j]<need_bucket:
                    need_upgrade+=need_bucket-bucket[j]
                # print(diff1,diff2,vat[j],i,bucket[j],ceil(vat[j]/i))
                # need_upgrade+=max(0,(vat[j]+i-1)//i-bucket[j])
            #print(i,need_upgrade)
            ans=min(ans,i+need_upgrade)
        return ans
# class Solution:
#     def storeWater(self, bucket: List[int], vat: List[int]) -> int:
#         mx = max(vat)
#         if mx == 0:
#             return 0
#         ans = inf
#         for x in range(1, mx + 1):
#             y = sum(max(0, (v + x - 1) // x - b) for v, b in zip(vat, bucket))
#             ans = min(ans, x + y)
#         return ans