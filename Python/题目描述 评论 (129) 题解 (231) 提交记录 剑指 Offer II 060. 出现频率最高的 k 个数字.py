class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        dict=defaultdict(int)
        heap=[]
        for num in nums:
            dict[num]+=1
        

        for k,v in dict.items():
            #print(k,v)
            #print(heap,len(heap))
            if len(heap)<K:
                heapq.heappush(heap,(v,k))
            else:
                if v>heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(v,k))
            #print(heap,len(heap))
        ans=heapq.nlargest(K,heap)
        for i in range(len(ans)):
            ans[i]=ans[i][1]
        return ans