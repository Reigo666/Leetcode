import numpy as np
from tqdm import tqdm
import csv

import sqlite3 as s

#隐马尔可夫模型
#面向命名实体识别(组织机构)问题
class HMM_BIO:
    def __init__(self,A=None,B=None,PI=None):
        #param:
        # (A,B,PI) 状态转移矩阵 发射矩阵 初始状态矩阵
        self.print=True
        
        
        self.N = 3     # 状态集合有多少元素(状态数BIO)
        self.M = 65535 # 观测集合有多少元素(汉字)
        
        #数字化 状态集合Q 观测集合V 
        self.status_dict={ # {'盒子1':0，'盒子2':1，'盒子3':2}
                        'B-ORG': 0,
                        'I-ORG': 1,
                        'O': 2}
        self.status=list(self.status_dict.keys())          
        #self.observe_dict={}# {'红':0，'白':1}
        self.Q=np.arange(0,self.N) #状态集合 [0,1,2]
        self.V=np.arange(0,self.M) #观测集合 [0,1]
        
        #初始化 (A,B,PI)
        self.A=A # 状态转移矩阵
        self.B=B # 发射矩阵
        self.PI=PI # 初始状态概率
        
        
        if self.print:
            print('状态集合status',self.status_dict)
            #print('观测集合observe',self.observe_dict)
            print('状态集合Q',self.Q)
            print('观测集合V',self.V)
            print()
        

    
    #训练模型(A,B,PI)
    #data (2,N)
    def train_bio(self,filename):
        self.calc_Param_bio(filename)
    
    
    def calc_Param_bio(self,filename):
        #利用数据data(状态序列+观测序列) 计算参数(A,B,PI) 直接使用统计方法 统计A,B,PI
        
        A=np.zeros((self.N,self.N)) #(N,N)
        B=np.zeros((self.N,self.M)) #(N,M)
        PI=np.zeros(self.N) #(N,)
        
        
        with open(filename,'r',encoding='utf-8') as fr:
            mult=10000000
            cnt=0
            
            line=fr.readline()
            pres=-1
            while line:
                mult-=1
                if mult==0:
                    cnt+=1
                    print(f'load {10000000}*{cnt} rows')
                    mult=10000000
                    
                
                
                s,v=line.split(',')
                s=int(s)
                v=int(v[:-1])
                #print(line,s,v)
                #当前为分隔符
                if s==-1 or v>=self.M:
                    pres=-1
                    line=fr.readline()
                    continue
                if pres!=-1:
                    #s 当前状态
                    #pres 上一次状态
                    #v 当前观测

                    A[pres,s]+=1
                    B[s,v]+=1
                    
                #上一个为分隔符
                else:
                    PI[s]+=1
                    B[s,v]+=1
                pres=s
                line=fr.readline()
        
        self.A=A
        self.B=B
        self.PI=PI
        
        self.normalize_param()
        print('训练参数结果(A,B,PI)')
        print(f'A:{self.A}')
        print(f'B:{self.B}')
        print(f'PI:{self.PI}')
        
        self.save_Param()
        
        
    
    def normalize_param(self):
        epsilon=1e-100
        
        
        self.PI[self.PI == 0] =epsilon  # 防止数据下溢,对数据进行对数归一化
        self.PI = np.log(self.PI) - np.log(np.sum(self.PI))

        self.A[self.A == 0] = epsilon
        self.A = np.log(self.A) - np.log(np.sum(self.A, axis=1, keepdims=True))

        self.B[self.B == 0] = epsilon
        self.B = np.log(self.B) - np.log(np.sum(self.B, axis=1, keepdims=True))
        
        #将(A,B,PI)归一化 (直接归一化)
        #self.A=self.A/np.sum(self.A,axis=1,keepdims=True)
        #self.B=self.B/np.sum(self.B,axis=1,keepdims=True)
        #self.PI=self.PI/np.sum(self.PI)

    def save_Param(self):
        np.savetxt('param/A.csv',self.A,delimiter=',')
        np.savetxt('param/B.csv',self.B,delimiter=',')
        np.savetxt('param/PI.csv',self.PI,delimiter=',')
        print('训练参数已保存在 param/A.csv')
        print()
    
    def load_Param(self,filename='param/'):
        self.A=np.genfromtxt(f'{filename}A.csv',delimiter=',')
        self.B=np.genfromtxt(f'{filename}B.csv',delimiter=',')
        self.PI=np.genfromtxt(f'{filename}PI.csv',delimiter=',')
        print(f'训练参数(A,B,PI)已从 {filename}A.csv 中读取成功')
        print()
    
    def viterbi_t(self,o):
        #维特比算法(动态规划)
        #已知(A,B,PI) 和一观测序列o 求解其状态序列的概率最大解
        #param:
        # o 观测序列 [0,1,1,1,1,0] shape(n,)
        #return:
        # ret 状态序列 shape(n,)
        #solution:
        # delta计算从前一个的所有状态 到当前状态的概率最大值 psi记录下来概率最大值的前一个状态
        # 从delta的最后取最大值，利用psi向前回溯即可找到最大概率序列
        
        n=o.shape[0]
        
        delta=np.zeros((self.N,n)) #delta[:,i] 为到达该观测序列的 每个状态的最大概率值 shape(状态个数,序列长度)
        psi=np.zeros((self.N,n),dtype=np.int32) #psi[:,i] 为到达该观测序列的 最大概率值的 上一个状态为哪个
        A=self.A
        B=self.B
        PI=self.PI
        
        #* -> + (因为log)
        delta[:,0]=PI+B[:,o[0]]
        #psi[:,0]=np.argmax(delta[:,0])
        for i in range(1,n):
            temp=delta[:,i-1]+A.T
            psi[:,i]=np.argmax(temp,axis=1)
            delta[:,i]=np.max(temp,axis=1)+B[:,o[i]]
            #check(delta)
            #check(psi)
        
        ret=np.zeros(n,dtype=np.int32)
        ret[-1]=np.argmax(delta[:,-1])

        for i in range(n-2,-1,-1):
            ret[i]=psi[ret[i+1]][i+1]
        return ret
    
    
    
    def calc_acc(self,label,predict):
        #计算标签预测的准确率
        #param:
        # a 源标签
        # b 目的标签
        return np.mean(np.equal(label,predict))
    
    def predict(self,s:str):
        #预测一段话的状态序列
        #param
        # s 一段中文
        #return
        # 中文加状态的文字 林B-LOC_|徽I-LOC_|因_O_|
        
        ans=""
        s=list(s)
        o=np.array([ord(ch) for ch in s])
        #print(o)
        statusList=self.viterbi_t(o)
        for i in range(len(s)):
            ans+=s[i]+str(self.status[statusList[i]])+'_|'
        #print(statusList)
        #print(ans)
        return statusList

#查看数组a1的属性
def check(a1):
    print(a1)  
    print("数据类型",type(a1))           #打印数组数据类型  
    print("数组元素数据类型：",a1.dtype) #打印数组元素数据类型  
    print("数组元素总数：",a1.size)      #打印数组尺寸，即数组元素总数  
    print("数组形状：",a1.shape)         #打印数组形状  
    print("数组的维度数目",a1.ndim)      #打印数组的维度数目
    print()

class s3db:
    """sqlite3数据库功能封装"""

    def __init__(self, dbpath=None):
        """如果构造时给出了数据库路径,则直接打开"""
        self.conn = None
        if dbpath is not None:
            self.open(dbpath)

    def opened(self):
        """判断是否打开了数据库"""
        return self.conn is not None

    def open(self, dbpath):
        """打开指定的数据库,返回值:是否成功"""
        if self.conn is not None:
            return True

        try:
            self.conn = s.connect(dbpath, check_same_thread=False)
            return True
        except Exception as e:
            return False

    def opt_set(self, cmd, val):
        """设定sqlite3配置参数,返回值:是否成功"""
        if self.conn is None:
            return False

        try:
            if not isinstance(val, str):
                val = str(val)
            self.conn.execute("PRAGMA  %s = %s" % (cmd, val))
            return True
        except Exception as e:
            return False

    def opt_def(self):
        """设置默认优化参数"""
        self.opt_set('Synchronous', 'OFF')
        self.opt_set('Journal_Mode', 'WAL')
        self.opt_set('Cache_Size', '16384')

    def close(self):
        """关闭数据库连接"""
        if self.conn is None:
            return True
        self.conn.close()
        self.conn = None

    def exec(self, sql, data=None, commit=True):
        """执行sql语句(不返回结果集的增删改语句).
            data - sql的绑定参数
            commit - 告知是否立即提交.不是立即提交时需要外部执行commit()方法手动提交,提高性能.
            返回值: (是否成功,错误消息)
        """
        try:
            if data is None:
                self.conn.execute(sql)
            else:
                self.conn.execute(sql, data)
            if commit:
                self.conn.commit()
            return True, ''
        except Exception as e:
            self.conn.rollback()
            return False, str(e)

    def commit(self):
        """手动提交执行结果.返回值(是否成功,错误消息)"""
        try:
            self.conn.commit()
            return True, ''
        except Exception as e:
            self.conn.rollback()
            return False, str(e)

class s3query:
    """sqlite3数据查询功能封装"""

    def __init__(self, db):
        """构造时绑定数据库对象"""
        self.db = db
        if db.conn:
            self.open(db)

    # 初始化查询对象,可指定数据库对象
    def open(self, db=None):
        """创建查询游标对象."""
        if db is None:
            db = self.db
        self.conn = db.conn
        self.cur = db.conn.cursor()

    def exec(self, sql, param=None, cmt=True):
        """执行sql语句,不要求获取结果集.
            返回值:成功时 - (True,影响的行数)
                  失败时 - (False,错误信息)
        """
        try:
            if param is None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, param)
            if cmt:
                self.conn.commit()
            return True, self.cur.rowcount
        except Exception as e:
            self.conn.rollback()
            return False, str(e)

    def query(self, sql, param=None, fetchsize=None):
        """执行sql查询,得到结果集(默认是得到全部,也可以指定获取的数量)
            返回值:成功时 - (结果集,'')
                  失败时 - (None,错误信息)
        """
        try:
            if param is None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql, param)
            if fetchsize is None:
                return self.cur.fetchall(), ''
            else:
                return self.cur.fetchmany(size=fetchsize), ''
        except Exception as e:
            return None, str(e)

    def fetch(self, fetchsize):
        """在query使用了fetchsize分批获取之后,继续获取结果集的后续部分
            返回值:成功时 - (结果集,'')
                  失败时 - (None,错误信息)
        """
        try:
            return self.cur.fetchmany(size=fetchsize), ''
        except Exception as e:
            return None, str(e)

    def append(self, obj, cmt=True):
        """轻量级ORM插入实现,obj的类型为表名,obj内含属性为表中字段与对应的值
            返回值:成功时 - (True,影响的行数)
                  失败时 - (False,错误信息)
        """

        def _insert(obj, cmt):
            tbl = type(obj).__name__
            val = []
            fds = []
            dmy = []
            for f in obj.__dict__:
                fds.append(f)
                val.append(obj.__dict__[f])
                dmy.append('?')
            sql = 'insert into %s (%s) values(%s)' % (tbl, ','.join(fds), ','.join(dmy))
            return self.exec(sql, val, cmt)

        if isinstance(obj, list) or isinstance(obj, tuple):
            for o in obj:
                _insert(o, False)
            if cmt:
                return self.db.commit()
            else:
                return True, ''
        else:
            return _insert(obj, cmt)

    def extract(self, sql, filter_fun, param=None, fetchsize=100):
        """执行查询,给出sql和参数param,对结果行进行filter_fun过滤,可设定提取批尺寸fetchsize.
           返回值:(结果数量,错误信息)
        """
        rc = 0
        rows, msg = self.query(sql, param, fetchsize)
        if msg: return rc, msg
        while len(rows):
            for row in rows:
                filter_fun(row)
                rc += 1
            rows, msg = self.fetch(fetchsize)
            if msg: return rc, msg
        return rc, msg

    def has(self, name, type='table'):
        """判断指定的库表对象table/index/view是否存在.
            返回值:None - 查询失败,结果未知
                  True/False - 告知是否存在
        """
        rows, msg = self.query("SELECT name FROM sqlite_master WHERE type=? and name=?", (type, name))
        if msg != '':
            return None
        return len(rows) > 0

    def close(self):
        """关闭数据查询对象"""
        if self.cur is not None:
            self.cur.close()
        self.cur = None
        self.conn = None
        self.db = None


#创建一个HMM模型用于命名实体识别
hmm_bio=HMM_BIO()
hmm_bio.load_Param('param/aft/')
#print(hmm_bio.predict("中国哈尔滨"))

#连接数据库
db=s3db('E:/DATA/Corporation/ner_data/samples.sqlite3')
print('connection:',db.opened())

#数据库sql操作
s3q=s3query(db)
sql='select * from tbl_datas'
q=s3q.query(sql)[0]
#print('Query:',q) #q:[(hash,title,text,corp,aft),(),()]

# 将text和corp对应并生成txt
for i in range(len(q)):
    hash=q[i][0]
    text=q[i][2]
    corp=q[i][3]

    textList=text.split('\n')
    nt_new=''
    for line in textList:
        if not line or line=='' or line=='\n':
            continue
        statuslist=hmm_bio.predict(line)
        l=0
        r=0
        
        while r<len(statuslist):
            l=r
            #如果当前状态不是O
            while r<len(statuslist) and statuslist[r]!=2:
                r+=1
            if r>l:
                nt_new+=line[l:r]+';'
            r+=1
    if len(nt_new)>=1:
        nt_new=nt_new[:-1]
    print(nt_new)
    sql=f'UPDATE tbl_datas SET nt_new = \'{nt_new}\' WHERE hash = \'{hash}\';'
    print(s3q.exec(sql))
        
        







