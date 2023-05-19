class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt=Counter(tiles)

        def dfs(cnt):
            ans=0
            for i,x in cnt.items():
                if x>0:
                    ans+=1
                    cnt[i]-=1
                    ans+=dfs(cnt)
                    cnt[i]+=1
            return ans


        return dfs(cnt)
        #A
        #A B
        #B A


        #B
        #A
        #A

        # A B AA AB     BA AAB ABA BAA
