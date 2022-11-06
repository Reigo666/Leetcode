class Solution:
    def interpret(self, command: str) -> str:
        temp=""
        ans=""
        for l in command:
            temp+=l
            if temp=="G":
                temp=""
                ans+="G"
            elif temp=="()":
                temp=""
                ans+="o"
            elif temp=="(al)":
                temp=""
                ans+="al"
        return ans