class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        G=defaultdict(list)
        for i in range(len(manager)):
            parent=manager[i]
            if parent>=0:
                child=i
                G[parent].append(child)
        
        def dfs(root):
            
            tempans=0
            for i in range(len(G[root])):
                tempans=max(tempans,dfs(G[root][i]))
                
            return tempans+informTime[root]
            
        return dfs(headID)
                