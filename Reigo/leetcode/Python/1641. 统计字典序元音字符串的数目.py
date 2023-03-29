class Solution:
    def countVowelStrings(self, n: int) -> int:
        # dict={'a':5,'e':4,'i':3,'o':2,'u':1}
        # arr=[5,4,3,2,1]
        if n==1:
            return 5
        vowel=[1,1,1,1,1]
        for i in range(1,n):
            #newvowel=[0,0,0,0,0]
            pre=0
            for j in range(5):
                pre+=vowel[j]
                vowel[j]=pre
            #print(vowel)
        return sum(vowel)