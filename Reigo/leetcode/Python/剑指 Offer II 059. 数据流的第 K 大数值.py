class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        heap=self.heap
        self.cap=k
        for i in range(len(nums)):
            if len(heap)<k:
                heapq.heappush(heap,nums[i])
            else:
                if nums[i]>heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,nums[i])

    def add(self, val: int) -> int:

        heap=self.heap
        #print(val,heap)
        if len(heap)<self.cap:
            heapq.heappush(heap,val)
        else:
            if val>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,val)
        return heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)