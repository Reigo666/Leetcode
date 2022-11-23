class TrieNode:
    def __init__(self):
        self.next={}
        self.isEnd=False
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        #[time,im,me,bell]
        #{t:[]}
        #
        #t i m e
        #b e l l
        #i m


        # def isMatch(word,curnode):
        #     for i in range(1,len(word)):
        #         l=word[i]
        #         if l not in curnode.next:
        #             return False
        #         curnode=curnode.next[l]
        #     return True
                    


        words.sort(key=lambda x:-len(x))
        root=TrieNode()

        ans=0
        for word in words:
            ismatch=False
            word=word[::-1]
            
            node=root

            ismatch=True
            for l in word:
                if l not in node.next:
                    ismatch=False
                    node.next[l]=TrieNode()
                #dict[l].append(node.next[l])
                node=node.next[l]
            if not ismatch: 
                ans+=len(word)+1
        #print(root.next)
        #print(dict)
        return ans
       
        
            
        
