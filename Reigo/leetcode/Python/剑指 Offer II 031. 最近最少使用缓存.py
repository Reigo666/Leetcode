class DlinkedList:
    def __init__(self,key,val,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=DlinkedList(-1,-1)
        self.tail=DlinkedList(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.val_node={}

    def get(self, key: int) -> int:
        val_node=self.val_node
        if key in val_node:
            node=val_node[key]
            self.moveToHead(node)
            return node.val
        else:
            return -1
    def put(self, key: int, val: int) -> None:
        val_node=self.val_node
        if key in val_node:
            node=val_node[key]
            self.removeNode(node)
            self.moveToHead(node)
            node.val=val
        else:
            newnode=DlinkedList(key,val)
            if len(val_node)<self.capacity:
                self.addToHead(newnode)
            else:
                rnode=self.removeTail()
                #print(val_node)
                del val_node[rnode.key]
                self.addToHead(newnode)
            val_node[key]=newnode

    def removeNode(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    def addToHead(self,node):
        next=self.head.next
        prev=self.head

        node.prev=prev
        node.next=next
        prev.next=node
        next.prev=node
    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)

    def removeHead(self):
        temp=self.head.next
        self.removeNode(self.head.next)
        return temp
    
    def removeTail(self):
        temp=self.tail.prev
        self.removeNode(self.tail.prev)
        return temp
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)