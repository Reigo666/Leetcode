class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]

        def backTrack(combination,left):
            if len(combination)>4:
                return
            if len(left)==0:
                if len(combination)==4:
                    ans.append(".".join(combination))
            else:
                for i in range(min(len(left),3)):
                    if i==0:
                        backTrack(combination+[left[:i+1]],left[i+1:])
                    else:
                        if left[0]!='0' and int(left[:i+1])<=255:
                            backTrack(combination+[left[:i+1]],left[i+1:])
        backTrack([],s)
        return ans