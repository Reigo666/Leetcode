from tqdm import tqdm
#读出corpus.txt 原始语料
with open('corpus.txt','r',encoding='utf-8') as fr:
    #写入八个文件
    for i in tqdm(range(8)):
        filename='corpus_part'+str(i)+'.txt'
        with open(filename,'w+',encoding='utf-8') as fw:
            #每个文件写出10行
            for j in range(171690180):
                cur=fr.readline()
                if not cur:
                    break
                fw.write(cur)
            while cur and cur!='\n':
                cur=fr.readline()
                fw.write(cur)
            if not cur:
                break
        break
