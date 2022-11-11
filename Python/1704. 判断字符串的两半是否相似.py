class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        vowel=set(['a','e','i','o','u'])
        n=len(s)//2
        num1=0
        num2=0

        for i in range(n):
            if s[i] in vowel:
                num1+=1
        for i in range(n,len(s)):
            if s[i] in vowel:
                num2+=1
        if num1==num2:
            return True
        return False
        print(s)