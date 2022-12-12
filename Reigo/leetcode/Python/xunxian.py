import bisect
from collections import defaultdict
import random

s="追风萌虎礼包,胧月鸮影,擎天巨神,秋夕葱聋,赤玉毒蝎,天穹神鹿,神鸟毕方,洪荒战兽,神威印记,仙魄碎片礼包（100枚),金霞珠,悟灵精魄,漓琰砂,天灵精魄,白色琅灵玉,金元仙粉残渣\
,陨擘精元,天宙石,星灵丹,司灵精魄,昀弦石,天亘石,璃霞精元,紫澜砂,晖鸣纹牌,陨霄石,兑洋银票(1砖),农政仙书,天绝石,十一阶绫橙石碎片,十一阶岚兵玦碎片,霞彩灵石,耀威破界石"

prob=[0.002,0.002,0.002,0.001,0.001,0.001,0.001,0.001,11.989,5.000,1.000,0.500,3.000,1,2,0.5,1,6,0.5,1.5,1,0.5,4,0.5,1,1,10,4,18,12,2,6,6]
items=s.split(",")
#print(len(prob),len(items),sum(prob))
dict={}
for i in range(len(items)):
    dict[items[i]]=prob[i]

left=[]
for i in range(len(prob)):
    if i==0:
        left.append(prob[i])
    else:
        left.append(prob[i]+left[-1])



def getOneItem():
    temp=random.uniform(0,100)
    #print(temp)
    idx=bisect.bisect(left,temp)
    #print(items[idx],prob[idx]/100)
    return items[idx]

def get_K_Items(k):
    res=defaultdict(int)
    for i in range(k):
        itemName=getOneItem()
        res[itemName]+=1
    return res

K=10000
print(get_K_Items(K))