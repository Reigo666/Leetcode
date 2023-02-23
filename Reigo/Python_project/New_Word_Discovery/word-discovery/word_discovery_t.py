import re
import glob
import math
from math import inf
from math import log
from math import exp



# 语料生成器，并且初步预处理语料
def text_generator(filename):
    '''每次选出一篇文章,每次返回一篇文章的处理后的字符串的一行'''
    #txts_path = glob.glob('corpus/short1/*.txt')#匹配所有文章
    #txts_path = glob.glob('corpus/THUCNews/THUCNews/eco/79*.txt')
    #txts_path = glob.glob('corpus/corporation/*.txt')
    # txts_path = glob.glob('corpus/corporation/nt_names_short.txt')
    #txts_path = glob.glob('corpus/corporation/nt_names.txt')
    txts_path = glob.glob(filename)
    for txt_path in txts_path:#每次选出一篇文章，对这一篇文章处理后,返回一篇文章的字符串
        f=open(txt_path,'r',encoding='utf-8')
        s = f.readline()
        while s:
            s = s.replace(u'\u3000', ' ').strip() #把中文空格转为英文空格
            s = re.sub(' ','',s) #把空格转为空
            s = re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z ]+', '\n', s)#将特殊字符转换为换行
            s=s.split('\n')
            for i in range(len(s)):
                yield s[i] #每次返回一行
            s = f.readline()

class TrieNode:
    '''特征树节点'''
    def __init__(self) -> None:
        self.next={}
        self.count=0 #记录词出现的次数
        self.solid=inf #记录词的凝固度
        self.free_degree=-1 #记录词的自由度(左熵右熵计算而得) 可以不记录左熵和右熵 记录的原因是可以看左熵和右熵的值 不记录的原因是可能增大空间开支
        #self.entrophy_right=-1 #记录词的左熵
        #self.entrophy_left=-1 #记录词的右熵
    
    def find_node(self,word):
        '''已知一个根节点,找当前根节点下的词,返回这个词对应的节点'''
        node=self
        for ch in word:
            if ch not in node.next:
                print(f'word {word} not in root')
                return None
            node=node.next[ch]
        return node

    def print_solid(self,print_num=200,N=4):
        '''打印print_num个词的凝固度 以凝固度降序排序 N为打印词的最大长度'''
        anslist=[]
        root=self
        def dfs(root,word):
            if len(word)>1:#只记录两字以上词的凝固度
                anslist.append([word,root.solid])
            if len(word)>=N:
                return
            for ch,node in root.next.items():
                dfs(node,word+ch)
        dfs(root,'')
        anslist.sort(key=lambda x:-x[1])#按照凝固度降序排序
        print('自由度')
        for i in range(print_num):
            print(anslist[i])
    
    def print_free_degree(self,print_num=200):
        '''打印print_num个词的自由度,左熵,右熵 以自由度降序排序 N为打印词的最大长度'''
        anslist=[]
        root=self
        def dfs(root:TrieNode,word,N=4):
            if len(word)>1:
                if hasattr(self,'entrophy_left'):
                    anslist.append([word,root.free_degree,root.entrophy_left,root.entrophy_right])
                else:
                    anslist.append([word,root.free_degree])
            if len(word)>=N:
                return
            for ch,node in root.next.items():
                dfs(node,word+ch)
        dfs(root,'')
        anslist.sort(key=lambda x:-x[1])#按自由度降序排序
        print('自由度,左熵,右熵')
        for i in range(print_num):
            print(anslist[i])

    def print_solid_and_free_degree(self,print_num=200,descent='solid',N=4):
        '''打印print_num个词的凝固度,自由度,左熵,右熵 以descent降序排序 N为打印词的最大长度'''
        'descent可以取值为solid 或 free_degree'
        if descent=='solid':
            descent=1
        elif descent=='free_degree':
            descent=2
        else:
            descent=1
        anslist=[]
        root=self
        def dfs(root:TrieNode,word):
            if len(word)>1:
                if hasattr(self,'entrophy_left'):
                    anslist.append([word,root.solid,root.free_degree,root.entrophy_left,root.entrophy_right])
                else:
                    anslist.append([word,root.solid,root.free_degree])
            if len(word)>=N:
                return
            for ch,node in root.next.items():
                dfs(node,word+ch)
        dfs(root,'')
        anslist.sort(key=lambda x:-x[descent])#按自由度降序排序
        print('凝固度,自由度,左熵,右熵')
        for i in range(print_num):
            print(anslist[i])
    
class NgramCount_t:
    '''统计词频,最多只统计长度为N,并且出现次数大于min_count次的词语'''
    def __init__(self,N=4,min_count=3) -> None:
        self.root=TrieNode()#根节点
        self.root.solid=-1 #根节点没有凝固度
        self.N=N #统计词的最大长度(在计算自由度时需考虑N+1个字)
        self.min_count=min_count #统计词的最少数量
        self.letterNum=0 #统计单个字的个数
    def do_count(self,txt):
        '''给定一整个txt文本或一行语句,统计词频'''
        root=self.root
        sentences=txt.split('\n')
        for sentence in sentences:
            for i in range(len(sentence)):
                node=root
                for j in range(i,min(i+self.N+1,len(sentence))):#记录N+1个字
                    ch=sentence[j]
                    if ch not in node.next:
                        node.next[ch]=TrieNode()
                    node=node.next[ch]
                    node.count+=1
                self.letterNum+=1
        self.root.count=self.letterNum
    def cut_tree(self,min_count=None):
        '''只保留树中出现次数大于等于min_count次的节点'''
        if min_count==None:
            min_count=self.min_count
        root=self.root
        def dfs(root,pre,curch):
            if 0<root.count<min_count:
                del root
                del pre.next[curch]
                return
            for ch in list(root.next.keys()):
                node=root.next[ch]
                dfs(node,root,ch)
        dfs(root,None,None)
    
    def print_count(self,min_count=None,print_all=False):
        '''打印出现次数大于等于min_count的词,如果print_all,则打印所有词语'''
        '''如果min_count为1即打印所有词'''
        if min_count==None:
            min_count=self.min_count
        if print_all:
            min_count=1
        root=self.root
        ansdict={}
        def dfs(root,word):
            if root.count>=min_count:
                ansdict[word]=root.count
            #已经次数小于min_count的词 后续节点一定小于min_count
            elif root.count!=0:
                return
            if len(word)==self.N:
                return
            for ch,node in root.next.items():
                dfs(node,word+ch)
        dfs(root,'')
        print(ansdict)

    
class solid_calc_t:
    '''计算凝固度类'''
    def __init__(self,root:TrieNode,min_proba={2:5, 3:25, 4:125},N=4) -> None:
        '''param: root:词典的特征树根节点,min_proba:凝固度阈值,限定词长N'''
        '''min_proba 字数对应凝固度边界 凝固度= p(x,y)/(p(x)*p(y)) = total*n(x,y)/(n(x)*n(y)) total为统计的总字数 记录在root.count中''' 
        '''凝固度越大 x和y越相关 凝固度越小 x和y越独立'''
        '''N为统计最大词长'''
        self.root=root
        self.min_proba = min_proba
        self.min_proba={2:1.2, 3:20, 4:30}
        self.N=N

        #处理min_proba中值不足的情况
        if len(self.min_proba)+1<self.N:
            if 2 not in self.min_proba:
                self.min_proba[2]=5
            for i in range(3,self.N+1):
                if i not in self.min_proba:
                    self.min_proba[i]=self.min_proba[i-1]*5
        
    def calc_solid(self):
        '''计算凝固度,返回凝固度符合的词列表'''
        '''核心思路 遍历根节点 记录以当前节点为分割节点时 所有子节点的凝固度值'''
        '''举例 例如'我吃饭'这一词 以我为分割点时 递归计算'我 吃'和'我 吃饭'的凝固度 '''
        '''递归到节点'我吃'时，以'我吃'为分割点计算'我吃 饭'的凝固度 这样'我吃饭'一词的凝固度即为以'我 吃饭'为分割点和'我吃 饭'为分割点的最小值 '''
        anslist=[]
        root=self.root

        def find_word_count(word):
            '''计算一个词出现的次数'''
            node=root
            for ch in word:
                if ch not in node.next:
                    print(f'word:{word} not in Dictionary')
                    return 0
                node=node.next[ch]
            return node.count

        def calc_back_fromCurNode(root,left_word):
            '''以当前root节点为分割点,计算所有后面节点的凝固度,left_word为当前节点代表的词语'''
            def dfs_calc(root:TrieNode,right_word,left_count,left_word):
                right_count=find_word_count(right_word) #计算分割点右侧词出现的次数
                word_count=root.count #当前整个词出现的次数
                solid=self.root.count*word_count/(left_count*right_count) #计算凝固度 total*n(x,y) / (n(x)*n(y))
                root.solid=min(root.solid,solid)

                if len(right_word)+len(left_word)==self.N:
                    return
                for ch,node in root.next.items():
                    dfs_calc(node,right_word+ch,left_count,left_word)

            for ch,node in root.next.items():
                dfs_calc(node,ch,root.count,left_word)


        def dfs(root,word):
            '''遍历所有节点,计算后面所有节点的凝固度'''
            if len(word)>0:
                calc_back_fromCurNode(root,word)
                if len(word)>=2 and root.solid>=self.min_proba[len(word)]:#词长度大于等于2 且词的凝固度符合要求
                    anslist.append([word,root.solid])
            if len(word)==self.N:#计算凝固度只计算最多N个字的情况
                return
            for ch,node in root.next.items():
                dfs(node,word+ch)

        dfs(root,'')
        anslist.sort(key=lambda x:-x[1])
        return anslist

    def print_word_solid(self,word):
        '''给定一个词，打印他的凝固度'''
        node=self.root
        for ch in word:
            if ch not in node.next:
                print(f'word:{word} not in root')
                return
            node=node.next[ch]
        print(node.solid)

    def print_solid(self,print_num=200):
        '''打印print_num个节点的凝固度'''
        anslist=[]
        def dfs(root,word):
            if len(word)>1:#只记录两字以上词的凝固度
                anslist.append([word,root.solid])
            if len(word)==self.N:#计算凝固度只计算最多N个字的情况
                return
            for ch,node in root.next.items():
                dfs(node,word+ch)
        dfs(self.root,'')
        anslist.sort(key=lambda x:-x[1])#按照凝固度降序排序
        print('凝固度')
        print(anslist[:print_num])



class free_degree_calc_t:
    '''根据正向词典和反向词典计算左右熵'''
    '''自由度计算方法为 获得一个词的左熵和右熵后 通过公式计算'''
    '''右熵=加和{p*(H(p))}'''
    '''H(p)为词的自信息=-ln(p)'''
    '''概率p为一个词某一个右字出现次数占所有该词右一字的数量总和'''
    def __init__(self,root_forward,root_backward,N=4) -> None:
        self.root_forward=root_forward #正向词典根节点
        self.root_backward=root_backward #反向词典根节点
        self.N=N #词的最大长度为N 但节点实际深度为N+1 为了计算N字词的右字
    
    def calc_word_free_degree(self,word):
        '''计算一个词的左熵和右熵,返回自由度,左熵,右熵'''

        entrophy_right=self.calc_word_entrophy(self.root_forward,word) #计算右熵
        entrophy_left=self.calc_word_entrophy(self.root_backward,word[::-1]) #计算左熵 需要在反向字典中查找反向词
        free_degree=self.calc_free_degree_by_SmoothNlp(entrophy_left,entrophy_right) #计算自由度

        return free_degree,entrophy_left,entrophy_right
        
    def calc_words_free_degree(self):
        '''遍历词典,计算所有词的自由度'''
        '''核心思想:右熵通过词典正向遍历时,已知该节点,调用calc_node_entrophy获得'''
        '''左熵通过词典正向遍历时,已知该词,将该词反转后,在反向词典树中调用calc_word_entrophy获得'''
        '''自由度由公式calc_free_degree_by_SmoothNlp计算而得'''
        root_forward=self.root_forward
        root_backward=self.root_backward
        
        def dfs(root,word):
            
            if len(word)>=2:
                #print('左熵,右熵,自由度')
                entrophy_right=self.calc_node_entrophy(root) #计算右熵
                entrophy_left=self.calc_word_entrophy(self.root_backward,word[::-1]) #计算左熵 需要在反向字典中查找反向词
                #print(word,entrophy_left,entrophy_right,end=' ')
                free_degree=self.calc_free_degree_by_SmoothNlp(entrophy_left,entrophy_right) #计算自由度
                #print(free_degree)
                root.entrophy_right=entrophy_right #左熵和右熵可以不记录
                root.entrophy_left=entrophy_left #
                root.free_degree=free_degree
                
            if len(word)==self.N:#计算自由度只计算最多N个字的情况
                return   

            for ch,node in root.next.items():
                dfs(node,word+ch)
        dfs(root_forward,'')
        
    def calc_node_entrophy(self,root:TrieNode):
        '''给定一个节点,计算该节点在树中的右熵,返回熵值'''
        cnt=0 #节点右邻字 字的总数
        entrophy=0 #熵值
        for node in root.next.values():
            cnt+=node.count
        
        for node in root.next.values():
            p=node.count/cnt
            entrophy+=p*self.calc_self_information(p)
        
        
        return entrophy


    def calc_word_entrophy(self,root:TrieNode,word):
        '''给定一个词典树和一个词,计算该词在树中的右熵'''
        '''用反向特征树词典计算的其实是该词在原正向树中的左熵'''
        node=root
        for ch in word:
            #print(ch)
            if ch not in node.next:
                print(f'word:{word} not in found root')
                return -1
            node=node.next[ch]
        entrophy=self.calc_node_entrophy(node)
        return entrophy

    
    def calc_self_information(self,p):
        '''给定一个概率,计算自信息的值'''
        return -math.log(p)
    
    def calc_free_degree_by_SmoothNlp(self,entrophy_left,entrophy_right):
        '''使用SmoothNlp计算公式在已知左熵和右熵的情况下计算自由度'''
        EL=entrophy_left
        ER=entrophy_right
        if EL==ER:#防止除以0
            return EL
        '''
        #为了适应特殊文本 例如文本某些字只出现在开头结尾的情况 开头结尾的字大多 会导致开头结尾词无左或右熵 自由度降低
        if EL==0:
            return ER
        if ER==0:
            return EL
        '''
        return log((EL*exp(ER)+ER*exp(EL))/abs(EL-ER))

    def calc_free_degree_by_HelloNLP(self,entrophy_left,entrophy_right):
        '''使用HelloNLP计算公式在已知左熵和右熵的情况下计算自由度'''
        '''此公式疑似有问题,但未找到正确公式,例如func(100,400)会出现负值'''
        EL=entrophy_left
        ER=entrophy_right
        if EL==0 and ER==0:
            return 1e-50
        if EL==ER:
            return EL
        if EL==0:
            EL=1e-100
        if ER==0:
            ER=1e-100
        ret=ER*log(EL/abs(EL-ER))+EL*log(ER/abs(EL-ER))
        return ret

    def print_free_degree(self,print_num=200):
        '''打印词的凝固度,自由度,左熵,右熵 以自由度降序排序'''
        anslist=[]
        root=self.root_forward
        def dfs(root:TrieNode,word):
            if len(word)>1:
                if hasattr(self.root_forward,'entrophy_left'):
                    anslist.append([word,root.solid,root.free_degree,root.entrophy_left,root.entrophy_right])
                else:
                    anslist.append([word,root.solid,root.free_degree])
            if len(word)==self.N:#计算凝固度只计算最多N个字的情况
                return
            for ch,node in root.next.items():
                dfs(node,word+ch)
        dfs(root,'')

        anslist.sort(key=lambda x:-x[2])#按自由度降序排序
        if hasattr(self.root_forward,'entrophy_left'):
            print('凝固度','自由度,左熵,右熵')
        else:
            print('凝固度','自由度')
        for i in range(min(print_num,len(anslist))):
            print(anslist[i])


class word_solid_free_degree_filter_t():
    '''根据凝固度和自由度和词的出现次数筛选词语'''
    '''筛选的项目包括凝固度,自由度,词的出现次数'''
    def __init__(self,root,min_proba={2:5, 3:25, 4:125},N=4) -> None:
        self.root=root
        self.min_proba=min_proba
        self.N=N

        #处理min_proba中值不足的情况
        if len(self.min_proba)+1<self.N:
            if 2 not in self.min_proba:
                self.min_proba[2]=5
            for i in range(3,self.N+1):
                if i not in self.min_proba:
                    self.min_proba[i]=self.min_proba[i-1]*5
    
    def filter_solid(self):
        '''对凝固度不满足的词语进行去除'''
        '''核心思想: 从子节点向父节点遍历(N+1个字的节点和)。当一个词凝固度满足条件时,他的孩子节点不能删除,因为要保存计算自由度。
        当一个词的凝固度不满足要求时,检查他的孩子节点凝固度是否满足,如果子节点凝固度存在1个满足的则该字就不能删除;如果所有孩子节点凝固度全不满足,则删除这个节点的所有孩子节点。'''
        '''能缩短搜索时间,减少字典占用空间。慎用,使用后不满足凝固度的节点会被永久删除,无法对这些词再进行后续调试'''
        def check_child_isDelete(root:TrieNode,word_length,rootch,word):
            '''检查所有孩子节点是否可以删除,如果可以,删除所有孩子节点,保留父节点root。word_length为到root节点的词的长度'''
            '''rootch为当前root所代表的字'''
            '''word_length为当前word的长度'''
            '''word为当前root所代表的词'''
            if word_length>self.N:#已经到叶子节点,叶子节点不能直接删除
                return False
            

            if word_length>=2 and root.solid>=self.min_proba[word_length]: #父节点凝固度满足条件 则无需删除所有子节点
                return False
            else: #父节点凝固度不满足条件
                isDelete=True
                if word_length==self.N:#已经是最长词的情况 直接删除所有子节点即可
                    pass
                else:#查看所有子节点是否满足凝固度要求
                    for ch,node in root.next.items():
                        if node.solid>=self.min_proba[word_length+1]:#有子节点不能删 那么父节点不能删 那么其他子节点也不能删除
                            return False
                #所有节点都不满足凝固度要求 删除所有子节点
                for ch,node in list(root.next.items()):
                    print(word+ch,word_length+1)
                    del node
                    del root.next[ch]
                
                if word_length==1:#词长为1的词已经没有子节点 可以删去
                    print(word,word_length)
                    del root
                    del self.root.next[rootch]
                return True

        root=self.root
        def dfs(root:TrieNode,word_length,rootch,word):
            for ch,node in list(root.next.items()):
                dfs(node,word_length+1,ch,word+ch)
            #遍历到最底层后开始反向删除
            if word_length!=0:#根节点不进行判断删除
                check_child_isDelete(root,word_length,rootch,word)
        dfs(root,0,'','')
    
    def select_valid_words(self,min_proba={2:5, 3:25, 4:125},free_degree_proba=0,count_limit=10000,print_num=inf):
        '''根据给定的凝固度阈值和自由度阈值和出现次数，对符合的词进行筛选'''
        '''print_num打印词的个数'''
        anslist=[]
        root=self.root
        def dfs(root:TrieNode,word):
            if len(word)>self.N:
                return
            if 2<=len(word)<=self.N:
                if root.solid>=min_proba[len(word)] and root.free_degree>free_degree_proba and root.count>=count_limit:
                    anslist.append([word,root.solid,root.free_degree,root.count])
            for ch,node in root.next.items():
                dfs(node,word+ch)
        dfs(root,'')
        print('词,凝固度,自由度,出现次数')
        for i in range(min(len(anslist),print_num)):
            print(anslist[i])
        return anslist

def check(word):
    nn=nc_forward.root.find_node(word)
    print(f'word:{word}')
    print('右熵',fdc.calc_word_entrophy(fdc.root_forward,word))
    print('左熵',fdc.calc_word_entrophy(fdc.root_backward,word[::-1]))
    print('凝固度,自由度,左熵,右熵,出现次数')
    sc.print_word_solid(word)
    print(fdc.calc_word_free_degree(word))
    if nn:
        print(nn.count)

if __name__=='__main__':
    #词频统计
    nc_forward=NgramCount_t(N=4) #用于计算凝固度 和右熵 (统计词的长度为4)
    nc_backward=NgramCount_t(N=4) #用于计算左熵
    txt_generator=text_generator('corpus/THUCNews/THUCNews/eco/79*.txt') #语料生成器
    #txt_generator=['四是四十一是十十四是十四四十一是四十一'] #可以用简单文章查看正确性

    print('Generate txts Fisish')
    print('running counting')
    cnt=0 #记录已经读取的行数
    cutcnt=200000 #多少行切割一次树
    epoch=1 #运行循环次数 计数cutcnt*epoch行后就退出 如果全部运行 调成epoch=-1即可
    min_count=4 #删去出现次数少于min_count的词

    #对文章进行正反统计
    for txt in txt_generator:
        cnt+=1
        if cnt%cutcnt==0: #cutcnt次后切割一次树
            print(txt)
            nc_forward.cut_tree(min_count)#删去出现次数少于min_count的词
            nc_backward.cut_tree(min_count)#删去出现次数少于min_count的词
            print(f'write {cnt//cutcnt}*{cutcnt} rows')
            if cnt==cutcnt*epoch:#运行cutcnt*epoch 行后就退出
                break
        
        nc_forward.do_count(txt)#将文章字加入计数
        nc_backward.do_count(txt[::-1])#将文章颠倒字加入计数

    nc_forward.cut_tree(min_count)#删去少于min_count的词
    nc_backward.cut_tree(min_count)#删去少于min_count的词
    print('Count word Finish')

    #nc_forward.print_count(min_count=3,print_all=False)#打印出现次数大于等于min_count的词
    print('Count letter number:',nc_forward.letterNum)#打印总共的字数


    sc=solid_calc_t(nc_forward.root) #创建计算凝固度类
    sc.calc_solid() #计算凝固度


    #打印词和凝固度 降序排序
    #sc.print_solid(print_num=100)


    #计算自由度
    fdc=free_degree_calc_t(nc_forward.root,nc_backward.root)
    fdc.calc_words_free_degree()


    #打印词的自由度 降序排序
    fdc.print_free_degree(print_num=200)

    
    #创建一个筛选合规词语的类
    wsfdf=word_solid_free_degree_filter_t(nc_forward.root)
    #wsfdf.filter_solid()  #删除不符合凝固度的词语 慎用
    wsfdf.select_valid_words(free_degree_proba=3,min_proba={2:5,3:17, 4:125},count_limit=1000) #选择符合规则的词语

    check('有限公司')



