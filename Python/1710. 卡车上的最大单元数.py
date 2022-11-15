class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        l=0
        ans=0
        while truckSize and l<len(boxTypes):
            if truckSize>=boxTypes[l][0]:
                truckSize-=boxTypes[l][0]
                ans+=boxTypes[l][0]*boxTypes[l][1]
            elif truckSize<boxTypes[l][0]:
                ans+=truckSize*boxTypes[l][1]
                truckSize=0
            l+=1
        return ans