class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        r=len(people)-1

        people.sort()
        ans=0
        while l<r:
            if people[l]+people[r]<=limit:
                l+=1
            
            r-=1
            ans+=1
        if l==r:
            ans+=1
        return ans