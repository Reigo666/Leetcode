class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen=set()
        for l in sentence:
            seen.add(l)
        if len(seen)==26:
            return True
        return False