class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict=defaultdict(int)
        ans1=[]
        ans2=[]
        for i in range(len(arr2)):
            dict[arr2[i]]=i
        
        for num in arr1:
            if num in dict:
                ans1.append(num)
            else:
                ans2.append(num)
        
        ans1.sort(key=lambda x:dict[x])
        ans2.sort()
        return ans1+ans2

