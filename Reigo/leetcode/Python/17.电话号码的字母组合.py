from typing import List
class Solution:
    #回溯
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        if digits=="":
            return ans
        num_alphabetdic={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        print(num_alphabetdic[2])
        #combination记录现有组合，digits记录剩余数字
        def backTrack(combination,digits):
            #终止条件，没有剩余数字，即将所有现有组合加入答案
            if len(digits)==0:
                ans.append(combination)
            #将当前digit加入组合
            else:
                for letter in num_alphabetdic[int(digits[0])]:
                    backTrack(combination+letter,digits[1:])
        backTrack("",digits)

        return ans
sol=Solution()
digits1 = "23"
digits2 = ""
digits3="2"

print(sol.letterCombinations(digits1))

#输入：digits = "23"
#输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]