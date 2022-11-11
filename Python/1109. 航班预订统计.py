class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dict=defaultdict(int)
        for b in bookings:
            dict[b[0]]+=b[2]
            dict[b[1]+1]-=b[2]
        
        temp=0

        #l=list(dict.keys())
        #l.sort()

        ans=[]
        
        for i in range(1,n+1):
            if i in dict:
                temp+=dict[i]
            ans.append(temp)
        
        return ans

        
        