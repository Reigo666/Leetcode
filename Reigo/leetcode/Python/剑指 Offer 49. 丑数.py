class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap=[]
        if n==1:
            return 1
        seen=set()
        seen.add(1)
        heapq.heappush(heap,1)

        temp=-1
        
        while n:
            temp=heapq.heappop(heap)
            if temp*2 not in seen:
                seen.add(temp*2)
                heapq.heappush(heap,temp*2)
            if temp*3 not in seen:
                seen.add(temp*3)
                heapq.heappush(heap,temp*3)
            if temp*5 not in seen:
                seen.add(temp*5)
                heapq.heappush(heap,temp*5)
            n-=1
        return temp