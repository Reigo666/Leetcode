class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k==0:
            return []
        heap=[]
        for num in arr:
            if len(heap)<k:
                heapq.heappush(heap,-num)
            else:
                if -heap[0]>num:
                    heapq.heappop(heap)
                    heapq.heappush(heap,-num)
        return [-num for num in heap]

