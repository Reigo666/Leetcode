class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for str in strs:
            st="".join(sorted(str))
            dict[st].append(str)
        
        return list(dict.values())