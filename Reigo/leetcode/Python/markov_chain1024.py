from itertools import permutations

def getNum(candi_nums, candi_ops):
    res = candi_nums[0]
    for i in range(3):
        res = eval('(' + str(res) + ')' + candi_ops[i] + '(' +str(candi_nums[i+1]) + ')')

    if res == 1024:
        print(candi_nums, candi_ops)
    


def get1024(nums, ops):
    candi_nums = list(permutations(nums, 4))
    candi_ops = list(permutations(ops, 3))
    
    for n in candi_nums:
        for o in candi_ops:
            getNum(n, o)

get1024([2,19,2,32,24,2,4,1,7,20,14,5,19,24,965], ['|','+','^'])
