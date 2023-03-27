class TrieNode:
    def __init__(self):
        self.next={}
        self.letter=None
        self.isEnd=False
        self.fail=None
        self.pre=None
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root=TrieNode()
        
        #创建Trie树
        for word in words:
            node=self.root
            for l in word:
                if l not in node.next:
                    node.next[l]=TrieNode()
                    node.next[l].letter=l
                    node.next[l].pre=node
                node=node.next[l]
            node.isEnd=True

        #创建Fail树
        q=deque([self.root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                for ch,nextnode in node.next.items():
                    q.append(nextnode)
                if node==self.root:
                    continue
                
                ch=node.letter
                #找到父节点fail节点
                fafail=node.pre.fail

                #遍历寻找fafail 直到找到fafail节点中含有ch的情况
                while fafail and ch not in fafail.next:
                    fafail=fafail.fail
                
                #父节点的fail节点为空 即父节点是root
                if not fafail:
                    node.fail=self.root
                else:
                    node.fail=fafail.next[ch]
                    if node.fail.isEnd:
                        node.isEnd=True
        self.queryNode=self.root

    def query(self, letter: str) -> bool:
        node=self.queryNode
        for ch in letter:
            while node and ch not in node.next:
                node=node.fail
            #root也没有ch
            if not node:
                self.queryNode=self.root
                return False
            #查找到字符ch
            else:
                self.queryNode=node.next[ch]
                if self.queryNode.isEnd:
                    return True
                else:
                    return False
        return None


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)