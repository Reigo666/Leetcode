# n为答题的人数
# right_people_list为每道题答对的人数
# qulified为合格的题数
def solveMaxValid(n,right_people_list,qulified):
    
    l=0
    r=n
    #sum_ans是总答对的题数
    sum_ans=sum(right_people_list)
    #一共的题数
    problems=len(right_people_list)

    def check(mid):
        left=sum_ans
        for i in range(problems):
            left-=min(mid,right_people_list[i])
        if (qulified-1)*(n-mid)>=left:
            return True
        else:
            return False
    while l<r:
        mid=(l+r)//2
        if check(mid):
            r=mid
        else:
            l=mid+1
    return l

# print(solveMaxValid(100,[74,79,81,85,91],3))
# print(solveMaxValid(100,[30,0,0,92,91],3))
print(solveMaxValid(100,[1,0,0,92,91],3))