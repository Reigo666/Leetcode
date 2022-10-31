


import collections


class LRUCache:
    dict={}
    que=collections.deque([])
    dictcapacity=0
    def __init__(self, capacity: int):
        self.dictcapacity=capacity
    def get(self, key: int) -> int:
        getvalue=self.dict.get(key,-1)
        if getvalue==-1:
            return -1
        else:
            self.que.remove(key)
            self.que.append(key)
            return getvalue

    def put(self, key: int, value: int) -> None:
        if key not in self.dict.keys():
            #位置已满
            if len(self.que)==self.dictcapacity:
                k=self.que.popleft()
                del self.dict[k]
                self.dict[key]=value
                self.que.append(key)

            #还有位置
            else:
                self.dict[key]=value
                self.que.append(key)

        else:
            #调整栈的位置
            self.dict[key]=value
            self.que.remove(key)
            
            self.que.append(key)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [   [2],    [1,0],[2,2],  [1], [3,3],[2],[ 4,4], [1],  [3],  [4]]
#[    null,    null,null,    0,    null,-1,  null, -1,     3,   4] answer
#[      null,   null,null,    0,   null,  2,  null,  0,    3    ,4]myans
# 解释
lrucache = LRUCache(2)
print(lrucache.put(1, 0))#缓存是 {1=1}
print(lrucache.put(2, 2))#缓存是 {1=1, 2=2}
print(lrucache.get(1))   #返回 1
print(lrucache.put(3, 3)) #该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
print(lrucache.get(2))   #返回 -1 (未找到)
print(lrucache.put(4, 4))  #该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
print(lrucache.get(1))   #返回 -1 (未找到)
print(lrucache.get(3))    #返回 3
print(lrucache.get(4))   #返回 4
lrucache = LRUCache(4)
a1=LRUCache(4)
print(lrucache.put(1, 0))#缓存是 {1=1}
print(lrucache.put(2, 2))#缓存是 {1=1, 2=2}
print(lrucache.get(1))   #返回 1
print(lrucache.put(3, 3)) #该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
print(lrucache.get(2))   #返回 -1 (未找到)
print(lrucache.put(4, 4))  #该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
print(lrucache.get(1))   #返回 -1 (未找到)
print(lrucache.get(3))    #返回 3
print(lrucache.get(4))   #返回 4
