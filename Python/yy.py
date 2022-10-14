



from collections import defaultdict


# birth=[1,2,8,15]
# death=[3,6,10,18]

birth=[]
death=[]
while True:
    try:
        
        a,b=[int(num) for num in input().strip().split()]
        birth.append(a)
        death.append(b)
        print(a+b)
    except EOFError: 
        break



dict=defaultdict(int)
for num in birth:
    dict[num]+=1

for num in death:
    dict[num]=-1

onbus=0
start=None

ans=0
years=list(dict.keys())
years.sort()
for year in years:
    onbus+=dict[year]
    if onbus!=0:
        if start==None:
            start=year
    else:
        ans+=year-start
        start=None
print(ans)

