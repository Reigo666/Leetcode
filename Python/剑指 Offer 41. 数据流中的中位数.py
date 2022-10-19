class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr=[]

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr,num)

    def findMedian(self) -> float:
        arr=self.arr
        n=len(arr)
        if n%2==1:
            return arr[n//2]
        else:
            return (arr[n//2-1]+arr[n//2])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()