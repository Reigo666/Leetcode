from collections import deque
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.next={}
        self.isEnd=False
        self.letter=None
        self.word=None
        self.information=[]

        self.fail=None
        self.pre=None

class Aho_Corasick_automaton:
    def __init__(self) -> None:
        self.root=TrieNode()

    #对words创建Trie树和Fail指针
    def create(self,words: List[str]):
        self.__createTrieTree(words)
        self.__createFail()

    #根据当前words创建Trie树
    def __createTrieTree(self,words: List[str]):
        root=self.root
        for word in words:
            node=root
            prenode=root
            cur=''
            for l in word:
                cur+=l
                if l not in node.next:
                    node.next[l]=TrieNode()
                node=node.next[l]
                node.letter=l
                node.word=cur
                node.pre=prenode
                prenode=node

            node.isEnd=True
            node.information.append(cur)
            
        #print(123)

    #在已有Trie树的情况下 给节点添加Fail指针
    def __createFail(self):
        root=self.root
        q=deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                for l in node.next:
                    q.append(node.next[l])
                if node==root:
                    continue
            
                fafail=node.pre.fail
                
                while fafail and node.letter not in fafail.next:
                    fafail=fafail.fail
                
                #root不包含node.letter
                if not fafail:
                    node.fail=root
                #node.letter in fafail
                else:
                    node.fail=fafail.next[node.letter]
                if node.fail.isEnd:
                    node.information.append(node.fail.word)
        #print(123)
    def parseText(self,word):
        root=self.root
        node=root
        ret=[]
        for l in word:
            #匹配不上就去fail
            while node and l not in node.next:
                node=node.fail
            
            #root也没有l
            if not node:
                node=root
                continue
            #node中有l
            else:
                node=node.next[l]
                #如果node有information
                if node.isEnd:
                    ret+=node.information
        return ret


            

ac=Aho_Corasick_automaton()
words=['he','she','hers','his']
parsetext1='ahishers'
parsetext2='ushers'
ac.create(words)
print(ac.parseText(parsetext1))#{his,she,he,hers}
print(ac.parseText(parsetext2))#{she,he,hers}



    