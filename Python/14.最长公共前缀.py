from typing import List

class Solution:
    #方法1 答案为初始化第一个 和第二个比较 剩下公共串 直到为0个 或到最后一个比较完
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        ans=strs[0]
        lens=len(strs)
        for i in range(1,lens):
            lens1=len(ans)
            lens2=len(strs[i])
            lenmin=min(lens1,lens2)
            ans=ans[0:lenmin]#先将答案缩短为公共长度
            for j in range(lenmin):
                if ans[j]!=strs[i][j]:
                    ans=ans[0:j]
                    break

            if ans=="":
                break
        return ans

    #方法2 使用python zip函数解包为('f', 'f', 'f') ('l', 'l', 'l') ('o', 'o', 'i') ('w', 'w', 'g')
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        ans=""
        zipped=zip(*strs)
        for tmp in zipped:
            tmp_set=set(tmp)
            if len(tmp_set)==0 or len(tmp_set)>=2:
                return ans
            else:
                ans+=tmp[0]      
        return ans
sol=Solution()
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
strs3 = ["ab", "a"]
print(sol.longestCommonPrefix1(strs1))
