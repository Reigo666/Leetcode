class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            matrix[i].insert(0,0)
            for j in range(1,n+1):
                matrix[i][j]=matrix[i][j-1]+matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum1=0
        matrix=self.matrix
        for i in range(row1,row2+1):
            sum1+=matrix[i][col2+1]-matrix[i][col1]
        return sum1

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)