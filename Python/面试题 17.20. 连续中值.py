class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr=[]

    def addNum(self, num: int) -> None:
        arr=self.arr
        bisect.insort(arr,num)

    def findMedian(self) -> float:
        arr=self.arr
        l=0
        r=len(arr)-1
        mid=(l+r)//2
        if len(arr)%2==0:
            return (arr[mid]+arr[mid+1])/2
        else:
            return arr[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()