class Solution:
    def findNthDigit(self, n: int) -> int:
        n=n+1
        sumbit=10
        bit=1

        mult=9

        while n>sumbit:
            mult*=10
            bit+=1
            n-=sumbit
            sumbit=bit*mult  
        
        if bit==1:
            temp_start_num=0
        else:
            temp_start_num=10**(bit-1)
        k=(n-1)//bit
        temp_num=temp_start_num+k
        n=n-k*bit
        return int(str(temp_num)[n-1])

            