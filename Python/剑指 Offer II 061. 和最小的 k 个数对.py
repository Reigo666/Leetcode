class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap=[]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                v1,v2=nums1[i],nums2[j]
                heapq.heappush(heap,((v1+v2,(v1,v2))))
        
        ans=[]
        for i in range(min(len(nums1)*len(nums2),k)):
            ans.append(list(heapq.heappop(heap)[1]))
        
        return ans