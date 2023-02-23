class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap=[]
        for class1 in classes:
            a,b=class1
            heapq.heappush(heap,(-(b-a)/(b*(b+1)),a,b))
        
        for i in range(extraStudents):
            temp=heapq.heappop(heap)
            t,a,b=temp
            a=a+1
            b=b+1
    
            newt=-(b-a)/(b*(b+1))
            #print(temp)
            #print(newt,a,b)
            #print()
            heapq.heappush(heap,(newt,a,b))
        
        ans=0
        N=len(heap)
        while heap:
            temp=heapq.heappop(heap)
            a,b,c=temp
            #print(temp)
            ans+=b/c
        return ans/N

        #2,3 3->4    0.66666 -> 0.75
        #3,5 4->6    0.6     -> 0.6666
        

