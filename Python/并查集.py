import collections
from typing import Collection,List
class Solution(object):
    def trulyMostPopular(self, names, synonyms):
        # 预处理
        f, cnt = {}, {}
        for name in names:
            n, c = name.split("(")
            f[n], cnt[n] = n, int(c[:-1])
        
        # 并查集查找同类根
        def find(x):
            if f[x] != x: f[x] = find(f[x])
            return f[x]

        for synonym in synonyms:
            name1, name2 = synonym.split(",")
            # 如果当前同类名不在公布名单中，则更新字典
            if f.get(name1[1:]) is None or f.get(name2[:-1]) is None: 
                if f.get(name1[1:]) is None:
                    f[name1[1:]] = name1[1:]
                    #cnt[name1[1:]]=0
                if f.get(name2[:-1]) is None: 
                    f[name2[:-1]] = name2[:-1]
                    #cnt[name2[:-1]]=0
            p1, p2 = find(name1[1:]), find(name2[:-1])
            # 保证同类根的字典序最小
            if p1 > p2: f[p1] = p2
            else: f[p2] = p1
        
        # 统计总频率
        ans = collections.defaultdict(int)
        for k, v in cnt.items():
            ans[find(k)] += v
        
        return [k+'('+str(v)+')' for k, v in ans.items()]



sol=Solution()
names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"] 
synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]

names1=["a(10)","c(13)"]
synonyms1=["(a,b)","(c,d)","(b,c)"]
print(sol.trulyMostPopular(names,synonyms))