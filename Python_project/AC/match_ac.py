
import record_log as reclog
import ac_Tree_forMatch as ac_tree
#Mine !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class ac_match_t():
    def __init__(self,rep_rec=reclog.rep_rec_t()):
        self.ac=ac_tree.Aho_Corasick_automaton() #ac自动机
        self.str_repl={} # 被替换词对应替换词字典
        self.rep_rec = rep_rec  # 替换记录器

        self.parsedTriples=[]  # 经过match解析后的三元组
        self.newParsedTriples=[] # 经过规则选择后的三元组
    #添加一组被替换词和替换词
    def dict_add(self, keyword, val='\x00', strip=True,keyword_lower=False):
        str_repl=self.str_repl
        if strip:
            keyword = keyword.strip()  # 关键词丢弃首尾空白
        if keyword_lower:
            keyword = keyword.lower()  # 关键词变小写
        
        str_repl[keyword]=val
    
    #在已经添加完所有被替换词后创建AC自动机
    def createAcTree(self):
        ac=self.ac
        str_repl=self.str_repl
        ac.create(str_repl.keys())

    #对message进行匹配解析
    def do_match(self, message):
        ac=self.ac
        rst = []
        def cb(b, e, v):
            rst.append((b, e, v))
        print(ac.parseText(cb,message))

        self.parsedTriples=rst
        print(rst)
    
    #对匹配好的所有三元组进行选择
    #__SELECT_MODE__={
    #   0 -> 前向最大化优先匹配(max_match)
    #   1 -> ??
    # }
    
    def do_select_triples(self,message,__SELECT_MODE__=0):
        #前向最大化优先匹配(max_match)
        #从前往后找最大长度的匹配
        rst=[]
        if __SELECT_MODE__==0:
            arr=sorted(self.parsedTriples,key=lambda x:(x[0],-x[1]))

            l=0
            while l<len(arr):
                end=arr[l][1]
                rst.append(arr[l])
                l+=1
                while l<len(arr) and arr[l][0]<end:
                    l+=1
            
            
        
        #补全三元组
        self.newParsedTriples=self.do_complete(message,rst)
        
        print(self.newParsedTriples)

    #将三元组没有替换的区域 添加为(s,e,None)
    def do_complete(self,message,triples):
        rst=[]
        if not triples:
            return
        
        if triples[0][0]>0:
            rst.append((0,triples[0][0],None))
        
        for i in range(len(triples)-1):
            rst.append(triples[i])
            if triples[i][1]<triples[i+1][0]:
                rst.append((triples[i][1],triples[i+1][0],None))
        rst.append(triples[-1])
        if triples[-1][1]<len(message):
            rst.append((triples[-1][1],len(message),None))

        return rst

    #对message进行替换
    def do_filter(self, message, repl="*"):
        rst=""
        npt=self.newParsedTriples
        for i in range(len(npt)):
            b,e,raw=npt[i]
            if raw==None:
                rst+=message[b:e]
            else:
                rst+=self.str_repl[raw]
        print(rst)
        return rst
        


if __name__ == '__main__':
    match = ac_match_t()
    match.dict_add('abcde', '12345')
    match.dict_add('abc', '123')
    match.dict_add('cde', '345')
    match.dict_add('bcd', '234')

    match.createAcTree()
    txt = "hello!abcde!abc!"

    #对message进行匹配解析为三元组
    match.do_match(txt)

    #选择一种选择策略生成新的三元组
    match.do_select_triples(txt)

    #对新的三元组中的词进行替换
    match.do_filter(txt)

    

#现在要做的事
#max_match
#is_all
#
"""基础方法,对给定的消息进行关键词匹配循环
        cb - 结果回调函数
        message - 待匹配的原文消息
        msg_len - 待匹配的原文消息字符长度
        offset - 从原文的指定偏移量进行匹配
        max_match - 是否进行关键词最大化优先匹配
        isall - 是否在最大化优先匹配的情况下记录同词根的短词匹配结果
        skip_match - 是否直接跳过已匹配的短语长度(提高速度,但可能丢弃中间短语) 不用要了
返回值:匹配次数"""