import csv
#7K
#file_read_path='BIO_train_pretreatment_1.csv'
#file_write_path='BIOES_train_pretreatment_1.csv'

#400M
# file_read_path='BIO_train_pretreatment_0.csv'
# file_write_path='BIOES_train_pretreatment_0.csv'

#9G
file_read_path='BIO_train_pretreatment.csv'
file_write_path='BIOES_train_pretreatment.csv'
with open(file_read_path,mode='r',encoding='utf-8') as fr:
    with open(file_write_path,mode='w',encoding='utf-8',newline='') as fw:
        cnt=10000000
        iii=0

        writer=csv.writer(fw)
        line=fr.readline()

        def parseLine(s):
            s=s.split(',')
            tag=s[0]
            ord=s[1][:-1]
            return int(tag),int(ord)
        while line:
            cnt-=1
            if cnt<0:
                cnt=10000000
                iii+=1
                print(f'write 100000000*{iii} rows')
            tag,ord=parseLine(line)
            if tag==-1 or tag==0:
                writer.writerow([tag,ord])
            elif tag==2:
                writer.writerow([3,ord])
            if tag==1:
                temp=[]
                while line and tag==1:
                    temp.append([tag,ord])
                    line=fr.readline()
                    tag,ord=parseLine(line)
                    cnt-=1
                temp[-1][0]=2
                writer.writerows(temp)
                continue
            line=fr.readline()

            
        